#! /usr/bin/env python3

from .gladeapp import GladeApp
import codecs

from gi.repository import Gtk


class FrobnicatorApp(GladeApp):

    UI_PATH = "/usr/share/frobnicator/frobnicator.ui"

    def __init__(self):
        super().__init__()
        self.textbuffer = self.get_widget("textview_file").get_buffer()
        self.get_widget("FrobnicatorAppWindow").show_all()
        self.filename = ""

    def get_buffer_text(self):
        return self.textbuffer.get_text(
                self.textbuffer.get_start_iter(),
                self.textbuffer.get_end_iter(),
                False)

    def set_buffer_text(self, text):
        self.textbuffer.set_text(text)

    def get_filename(self, action):
        if action == Gtk.FileChooserAction.OPEN:
            msg = "Please choose a file"
            btn_text = Gtk.STOCK_OPEN
        elif action == Gtk.FileChooserAction.SAVE:
            msg = "Save as..."
            btn_text = Gtk.STOCK_SAVE
        else:
            msg = "File chooser"
            btn_text = "Weird"

        chooser = Gtk.FileChooserDialog(
                msg,
                self.get_widget("FrobnicatorAppWindow"),
                action,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                    btn_text, Gtk.ResponseType.OK))

        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            result = chooser.get_filename()
        else:
            result = None

        chooser.destroy()
        return result

    def prompt_save(self):
        dialog = Gtk.Dialog(
                "Unsaved Changes",
                self.get_widget("FrobnicatorAppWindow"), 0,
                (Gtk.STOCK_YES, Gtk.ResponseType.YES,
                 Gtk.STOCK_NO, Gtk.ResponseType.NO))

        label = Gtk.Label("Save changes?")
        box = dialog.get_content_area()
        box.add(label)
        dialog.show_all()

        response = dialog.run()

        if response == Gtk.ResponseType.YES:
            self.on_toolbutton_save_clicked()

        dialog.destroy()

    def on_toolbutton_new_clicked(self, *args):
        if self.textbuffer.get_modified() and (self.get_buffer_text() or self.filename):
            self.prompt_save()
        self.set_buffer_text("")
        self.textbuffer.set_modified(False)

    def on_toolbutton_open_clicked(self, *args):
        if self.textbuffer.get_modified() and (self.get_buffer_text() or self.filename):
            self.prompt_save()

        self.filename = self.get_filename(Gtk.FileChooserAction.OPEN)
        with open(self.filename) as fh:
            self.set_buffer_text(fh.read())

        self.textbuffer.set_modified(False)

    def on_toolbutton_save_clicked(self, *args):
        if not self.filename:
            self.filename = self.get_filename(Gtk.FileChooserAction.SAVE)
            if self.filename == None:
                self.filename = ""
                return

        with open(self.filename, 'w') as fh:
            fh.write(self.get_buffer_text())

        self.filename = ""
        self.textbuffer.set_modified(False)

    def on_button_reverse_clicked(self, *args):
        self.set_buffer_text(''.join(reversed(self.get_buffer_text())))

    def on_button_rot13_clicked(self, *args):
        self.set_buffer_text(codecs.encode(self.get_buffer_text(), 'rot_13'))

    def on_button_frobnicate_clicked(self, *args):
        self.on_button_reverse_clicked(*args)
        self.on_button_rot13_clicked(*args)


def main():
    FrobnicatorApp().run()


if __name__ == "__main__":
    main()
