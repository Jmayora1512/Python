import cv2
import cv2.cv as cv
import numpy
import zbar
import time
import threading

class BarCodeScanner(threading, Thread):
   def _init_(self):
      threading.Thread._init_(self)
      self.WINDOW_NAME = 'Camera'
      self.CV_SYSTEM_CACHE_CNT = 5 #Cv has5-frame cache

      cv.NamedWindow(self.WINDOW_NAME, cv.CV_WINDOW_NORMAL)
      self.cam = cv2.VideoCapture(-1)

   def scan(self, aframe):
      imgray = cv2.cvtColor(aframe, cv2.COLOR_BGR2GRAY)
      raw = str(imgray.data)
      
      scanner = zbar.ImageScanner()
      scanner.parse_config('enable')

      print ('ScanZbar time.time())
      width = int(self.cam.get(cv.CV_CAP_PROP_FRAME_WIDTH)
      height = int(self.cam.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
      imageZbar = zbar.Image(width, height, 'Y800', raw)
      imageZbar = zbar.Image(width, 'Y800', raw)
      scanner.scan(imageZbar)
      print ('ScanEnd', time.time())

   for symbol in imageZbar:
      print ('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)

   def run(self):
      print ('BarCodeScanner run', time.time())
      while True:
	print (time.time())
	for i in range(0,self.CV_SYSTEM_CACHE_CNT):
	   print ('Read2Throw', time.time())
	   self.cam.read()
	print ('Read2Use', time.time())
	img = self.cam.read()
	self.scan(img[1])

	cv2.imshow(self.WINDOW_NAME, img[1])
	cv.WaitKey(1)
	print ('Sleep', time.time())
	time.sleep(self.LOOP_INTERVAL_TIME)

   cam.release()

scanner = BarCodeScanner()
scanner.start()
      


