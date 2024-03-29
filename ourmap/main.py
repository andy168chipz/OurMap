#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import webapp2
import jinja2
import os
from google.appengine.ext import db
from google.appengine.api import memcache #if deployed google do it for you
from handlers.base import *
from handlers.image import *



app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/about', AboutHandler),
	('/testing', testingHandler),
	('/image', imageHandler)

], debug=True)
