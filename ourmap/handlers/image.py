__author__ = 'andychou'

from base import Handler

class imageHandler(Handler):
	def get(self):
		#return self.write("hello")
		pass
	def post(self):
		return self.write("post")