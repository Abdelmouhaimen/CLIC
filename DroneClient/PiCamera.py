from picamera2 import Picamera2

class PiCamera:
    def __init__(self,width=32, height=32):
        self.picam2 = Picamera2()
        config = self.picam2.create_preview_configuration(main={"size": (32, 32), "format": "RGB888"})
        self.picam2.configure(config)
        self.picam2.start()


    def get_frame(self):
        return self.picam2.capture_array()
    
    def close(self):
        self.picam2.stop()

    

