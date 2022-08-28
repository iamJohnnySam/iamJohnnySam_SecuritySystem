import tensorflow as tf

class CCTVclassify:

    def __init__ (self, tfLocation):
        self.model = tf.lite.Interpreter(model_path=tfLocation)
        self.model.allocate_tensors()
        self.input_details = self.model.get_input_details()
        self.output_details = self.model.get_output_details()