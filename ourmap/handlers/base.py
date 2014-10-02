__author__ = 'Andy'

#
import webapp2
from google.appengine.api import users
import jinja2
import os
import logging

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
		self.render("map.html")

class AboutHandler(Handler):
	def get(self):
		self.render("about.html")

class testingHandler(Handler):
	def get(self):
		user = users.get_current_user()
		if user:
			greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
		else:
			greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
		self.response.out.write("<html><body>%s</body></html>" % greeting)