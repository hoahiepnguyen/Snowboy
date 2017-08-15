import dbus
import dbus.service
import dbus.glib


class Emitter(dbus.service.Object):
	"""Emitter DBUS service object."""

	def __init__(self, bus_name, object_path):
		"""Initialize the emitter DBUS service object."""
		dbus.service.Object.__init__(self, bus_name, object_path)

	@dbus.service.signal('tld.domain.sub.event')
	def Signal(self, message):
		""" The signal is emitted when this method exits"""
		""" You can have code here if you wish """
		pass

	@dbus.service.signal('tld.domain.sub.event')
	def emitSignal(self):
		# emit signals by calling the signal's skeleton method
		self.Signal('Hello alexa')
		print 'Singal emitted'

	@dbus.service.signal('tld.domain.sub.event')
	def quit_signal(self):
		"""Emmit a quit signal."""
		print 'Emitted a quit signal'
