import imaplib
import smtplib, ssl
import email
import os
import numpy as np
import shutil
import logging

from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate

from PIL import Image, ImageOps

from .CCTVclassify import CCTVclassify

class CCTVEmailManager ():
    att_path = "No attachment found."
    fldCCTVDownload = "log/CCTV/Download"
    foldersize = 0

    em = 'autonomation@outlook.com'
    pw = 'B00b!es@44'

    def __init__(self, folder):
        self.initialize(folder)

    def initialize (self, folder):

        self.outlook = imaplib.IMAP4_SSL('outlook.office365.com', 993)
        self.outlook.login(self.em, self.pw)
        self.outlook.select(mailbox = folder, readonly=False)

        self.dirname = os.path.dirname(__file__)

        self.modelA01 = CCTVclassify(os.path.join(self.dirname, 'tfModels/model1.tflite'))
        self.modelA02 = CCTVclassify(os.path.join(self.dirname, 'tfModels/model1.tflite'))

        if os.path.isdir(self.fldCCTVDownload):
            for f in os.listdir(self.fldCCTVDownload):
                self.foldersize = self.foldersize + os.path.getsize(os.path.join(self.fldCCTVDownload, f))
        else:
            os.makedirs(self.fldCCTVDownload)

    def close_connection(self):
        self.outlook.connection.close()

    def runCCTV(self):
        (result, messages) = self.outlook.search(None, 'UnSeen')

        if result == "OK":
            for message in messages[0].split():
                try: 
                    ret, data = self.outlook.fetch(message,'(RFC822)')
                except:
                    logging.info("No new emails to read.")
                    self.close_connection()

                msg = email.message_from_bytes(data[0][1])
                Date = msg['Date']
                Date = Date.replace(" +0530", "")
        
                for part in msg.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    self.assessAttachment(part, Date)

                ret, data = self.outlook.store(message, '+FLAGS','\\Deleted')

    def assessAttachment(self, part, Date):

        filename = part.get_filename()
        saveas = Date+" "+filename
        self.att_path =os.path.join(self.fldCCTVDownload, saveas)
            
        image = part.get_payload(decode=True)
        fp = open(self.att_path, 'wb')
        fp.write(image)
        fp.close()
            
        # Prepare Image
        img = Image.open(self.att_path)
        img = ImageOps.grayscale(img)
        img = np.asarray(img,dtype="float32")/255
        img = np.expand_dims(img, axis=0)
            
        Sus = False
        # ML CODE
        output = 0.000001

        if "A01" in filename:
            output = self.modelA01.classify (img)
            if (output > 0.95):
                Sus = True
            
        if "A02" in filename:
            output = self.modelA02.classify (img)
            if (output > 0.95):
                Sus = True
            
        if not Sus:
            os.remove(self.att_path)
                        
        if Sus:
            foldersize = foldersize + os.path.getsize(self.att_path)
            print(filename, output, "{:,}".format(foldersize))


    def sendSus(self):
        send_to = ['john.samarasinghe@outlook.com', 'gayathri_karunaratne@yahoo.com']

        if (self.foldersize > 0):
            send_from = self.em
            body = """\
                <html>
                    <body>
                        <p>Hi mau mau and mau,<br>
                           We detected some activity outside the gate in the last 1 hour.<br>
                        </p>
                    </body>
                </html>
            """
    
            msg = MIMEMultipart()
            msg['From'] = send_from
            msg['To'] = ", ".join(send_to)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = "Suspicious Activity at 110/2"
    
            msg.attach(MIMEText(body, "html"))
    
            size = 0
            for f in os.listdir(self.fldCCTVDownload):
                with open(os.path.join(self.fldCCTVDownload, f), "rb") as fil:
                    part = MIMEApplication(fil.read(),Name=basename(f))
                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)
                size = size + os.path.getsize(os.path.join(self.fldCCTVDownload, f))
                foldersize = foldersize - os.path.getsize(os.path.join(self.fldCCTVDownload, f))
                # os.remove(os.path.join(self.fldCCTVDownload, f))
                shutil.move(os.path.join(self.fldCCTVDownload, f), os.path.join(self.fldCCTVDownload, f))
                if (size > (4.9*1024*1024)):
                    break


            context = ssl.create_default_context()
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.starttls(context=context)
            server.login(self.em, self.pw)
            server.sendmail(send_from, send_to, msg.as_string())
            server.close()