__author__ = 'andychou'

from base import Handler
import logging




class imageHandler(Handler):
	def get(self):
		#return self.write("hello")
		self.redirect("/")
		pass
	def post(self):
		data = self.request.get('state')
		logging.error(data)
		#state = data.name
		return self.write("success" + data)
	def query_image(self, state):
		pass