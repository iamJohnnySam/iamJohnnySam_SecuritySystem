import imaplib
import email
import time
import numpy as np
import shutil
from ..Global.globalVariables import *


output = 0.000001
foldersize = 0

from PIL import Image, ImageOps

def outlookConnect ():
    outlook = imaplib.IMAP4_SSL('outlook.office365.com', 993)
    outlook.login(em, pw)
    outlook.select(mailbox = 'Security', readonly=False)

def outlookGetCCTV ():
    (result, messages) = outlook.search(None, 'UnSeen')
    if result == "OK":
        for message in messages[0].split():
            try: 
                ret, data = outlook.fetch(message,'(RFC822)')
            except:
                print("No new emails to read.")
                outlook.connection.close()
                exit()

            msg = email.message_from_bytes(data[0][1])
            Date = msg['Date']
            Date = Date.replace(" +0530", "")
        
            att_path = "No attachment found."
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                saveas = Date+" "+filename
                att_path = os.path.join(download_folder, saveas)
            
                image = part.get_payload(decode=True)
                fp = open(att_path, 'wb')
                fp.write(image)
                fp.close()
            
                # IMAGE
                img = Image.open(att_path)
                img = ImageOps.grayscale(img)
                img = np.asarray(img,dtype="float32")/255
                img = np.expand_dims(img, axis=0)
            
                Sus = False
                # ML CODE
                if "A01" in filename:
                    modelA01.set_tensor(input_details1[0]['index'], img)
                    modelA01.invoke()
                    output_data = modelA01.get_tensor(output_details1[0]['index'])
                    output = output_data[0][0]
                    if (output > 0.95):
                        Sus = True
            
                if "A02" in filename:
                    modelA02.set_tensor(input_details2[0]['index'], img)
                    modelA02.invoke()
                    output_data = modelA02.get_tensor(output_details2[0]['index'])
                    output = output_data[0][0]
                    if (output > 0.95):
                        Sus = True
            
                if not Sus:
                    os.remove(att_path)
                        
                if Sus:
                    foldersize = foldersize + os.path.getsize(att_path)
                    print(filename, output, "{:,}".format(foldersize))

            response, data = outlook.store(message, '+FLAGS','\\Deleted')

outlookDisconnect():
    outlook.close()

send_to = ['john.samarasinghe@outlook.com', 'gayathri_karunaratne@yahoo.com']

if (foldersize > 0):
    print("Sending email")
    import smtplib, ssl
    from os.path import basename
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.utils import COMMASPACE, formatdate
    
    send_from = em
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
    for f in os.listdir(download_folder):
        with open(os.path.join(download_folder, f), "rb") as fil:
            part = MIMEApplication(fil.read(),Name=basename(f))
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
        size = size + os.path.getsize(os.path.join(download_folder, f))
        foldersize = foldersize - os.path.getsize(os.path.join(download_folder, f))
        # os.remove(os.path.join(download_folder, f))
        shutil.move(os.path.join(download_folder, f), os.path.join(save_folder, f))
        if (size > (4.9*1024*1024)):
            break


    context = ssl.create_default_context()
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls(context=context)
    server.login(em, pw)
    server.sendmail(send_from, send_to, msg.as_string())
    server.close()