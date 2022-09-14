import tensorflow as tf

class CCTVclassify:
    def __init__ (self, tfLocation):
        self.model = tf.lite.Interpreter(model_path=tfLocation)
        self.model.allocate_tensors()
        #self.input_details = self.model.get_input_details()
        self.output_details = self.model.get_output_details()

    def classify (self, img):
        self.model.set_tensor(self.input_details[0]['index'], img)
        self.model.invoke()
        output_data = self.model.get_tensor(self.output_details[0]['index'])
        output = output_data[0][0]
        return output