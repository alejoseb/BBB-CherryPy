import os, os.path
import cherrypy

class bbbPage(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class bbbPageWebService(object):
    
     exposed = True
     @cherrypy.tools.accept(media='text/plain')
     def PUT(self, x, y):
       # self.blinkLed()
        print "x: "+ str(x) +" y: " + str(y) 
	print "Opening the file..."
	target = open('./log.txt', 'a')
	target.write('X:' +  str(x) + ' ,Y:'+str(y) +'\n')
        target.close()
 	return "x: "+ str(x) +" y: " + str(y)             
     
     def ON(self):
        #GPIO.output("P9_14", GPIO.HIGH)
        print "Led on" 
        return "Led on"    
        
     def OFF(self):
        #GPIO.output("P9_14", GPIO.LOW)
        print "Led off" 
        return "Led off"    
    
     def BLINK(self):
        #self.blinkLed()
        print "Led BLINKING" 
        return "Led BLINKING" 


     def LEER(self):
        print "Reading text"
	f =open('./log.txt')
        texto=''
	for line in f:
		texto=texto+line 
        return texto        

if __name__ == '__main__':
     conf = {
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
#     GPIO.setup("P9_14", GPIO.OUT)
     webapp = bbbPage()
     webapp.generator = bbbPageWebService()
     cherrypy.config.update({'server.socket_host': '0.0.0.0'})
     cherrypy.quickstart(webapp, '/', conf)
