from pox.core import core
from pox.openflow_discovery import Discovery
from pox.lib.revent import *
from pox.lib.recoco import Timer 

class Test1(EventMixin):
	def init(self):
		Timer(30,"request_links",recurring = True)

	def request_links(self):
		print "requesting timer"
def launch():
	core.registerNew(Test1)

