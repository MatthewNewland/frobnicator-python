import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GladeApp:

    def __init__(self):
        """
        Load a UI definition file specified by path, and connect signals.
        """
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.__class__.UI_PATH)
        self.builder.connect_signals(self)

    def quit(self):
        Gtk.main_quit()

    def run(self):
        Gtk.main()

    def get_widget(self, name):
        return self.builder.get_object(name)

    def get_widgets(self):
        return self.builder.get_objects()

    def gtk_main_quit(self, *args):
        self.quit()

    def gtk_widget_destroy(self, widget, *args):
        widget.destroy()
