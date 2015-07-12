import cherrypy
import pmxbot

from jaraco.pmxbot import http

pmxbot.config['BitBucket channels'] = dict(default='default')

class Server(http.Server):
	def send_to(self, channel, *msgs):
		print("Message for", channel)
		for msg in msgs:
			print(msg)

if __name__ == '__main__':
	Server.start(log_screen=True)
	cherrypy.engine.block()
