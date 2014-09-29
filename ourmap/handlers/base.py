__author__ = 'Andy'

#
import webapp2

import jinja2
import os


template_dir = os.path.join(os.path.dirname(__file__), '../templates')  #path to template_dir, __file__(dir of cur file)
#set up jinja_env w/ template dir
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(Handler):
	def get(self):
		self.render("base.html")

class AboutHandler(Handler):
	def get(self):
		self.render("about.html")