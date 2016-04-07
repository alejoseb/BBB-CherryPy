import os, os.path
import cherrypy
import Adafruit_BBIO.GPIO as GPIO
import time

class bbbPage(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class bbbPageWebService(object):
     exposed = False
     def blinkLed(self):
        for x in range(1,5):
            GPIO.output("P9_14", GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output("P9_14", GPIO.LOW)
            time.sleep(0.1)   
        return
    
     exposed = True
     @cherrypy.tools.accept(media='text/plain')
     def PUT(self, x, y):
        self.blinkLed()
        print "x: "+ str(x) +" y: " + str(y) 
        return "x: "+ str(x) +" y: " + str(y)   
     
     def ON(self):
        GPIO.output("P9_14", GPIO.HIGH)
        print "Led on" 
        return "Led on"    
        
     def OFF(self):
        GPIO.output("P9_14", GPIO.LOW)
        print "Led off" 
        return "Led off"    
    
     def BLINK(self):
        self.blinkLed()
        print "Led BLINKING" 
        return "Led BLINKING" 
         

if __name__ == '__main__':
     conf = {
        #'/': {
        #     'tools.sessions.on': True,
        #     'tools.staticdir.root': os.path.abspath(os.getcwd())
        #},
        '/': {
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/generator': {
             'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
             'tools.response_headers.on': True,
             'tools.response_headers.headers': [('Content-Type', 'text/plain')]
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         }
       
         
         
     }
     GPIO.setup("P9_14", GPIO.OUT)
     webapp = bbbPage()
     webapp.generator = bbbPageWebService()
     cherrypy.config.update({'server.socket_host': '0.0.0.0'})
     cherrypy.quickstart(webapp, '/', conf)
