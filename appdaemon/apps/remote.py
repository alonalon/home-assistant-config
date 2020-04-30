from entities import Entities

class Remote(Entities):
	def initialize(self):
		super().initialize()

		self.listen_event(self.event, 'zha_event')

	def event(self, ev, data, kwargs):
		command = data.get('command');
		if command == 'on':
			self.turn_on("light.kitchen_lights")
		if command == 'step':
			self.log('STEP!!')
			self.log(data)
		if command == 'off_with_effect':
			self.turn_off("light.kitchen_lights")
