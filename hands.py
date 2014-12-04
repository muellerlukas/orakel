# -*- coding: utf-8 -*-
# vim:set ts=8 sts=8 sw=8 tw=80 noet cc=80:

from time import time

class Hands(object):
	def __init__(self, storage, config):
		self.storage = storage
		self.config = config
		try:
			self.storage['lasthands']
		except:
			self.storage['lasthands'] = 0

	def action(self, msg, nick, send_message):
		try:
			hands = {'o/':'\o','\o':'o/','\o/':'\o/'}
			if msg in hands:
				send_message(hands.get(msg))
			return True
		except:
			return False

	def __call__(self, msg, nick, send_message):
		if not self.config.intrusive:
			return False
		t = time()
		if (t - self.storage['lasthands']) < \
				self.config.getint("timeouts", "hands"):
			return False
		if not self.action(msg, nick, send_message):
			return False
		self.storage['lasthands'] = t
		return True
