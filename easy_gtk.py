__version__: "0.1"
__author__: "noxonsoftwares"
__web__: "www.noxonsoftwares.blogspot.com"


import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk




class Controles:
    def agregar_box(self, espacio):
        self.box = Gtk.Box(spacing=espacio)
        self.add(self.box)

    def agregar_btn_en_box(self, nom_btn, texto, evento, accion):
        nom_btn= Gtk.Button(label=texto)
        nom_btn.connect(evento, accion)
        self.box.pack_start(nom_btn, True, True, 0)

    def agregar_lbl_en_box(self, nom_lbl, texto, angulo, halign):
        nom_lbl = Gtk.Label()
        nom_lbl.set_label(texto)
        nom_lbl.set_angle(angulo)
        nom_lbl.set_halign(Gtk.Align(halign)) # 0 = Centrado - 1 = Izquierda - 2 = Derecha
        self.box.pack_start(nom_lbl, True, True, 0)


class MessageInfo:
    def msg_info(self, txt_prin, txt_sec):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=txt_prin,
        )
        dialog.format_secondary_text(
            txt_sec
        )
        dialog.run()
        dialog.destroy()

    def msg_inf_ok_cancel(self, txt_prin, txt_sec, respYES, respNO):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.YES_NO,
            text=txt_prin,
        )
        dialog.format_secondary_text(
            txt_sec
        )
        respuesta = dialog.run()
        if respuesta == Gtk.ResponseType.YES:
            respYES()
        elif respuesta == Gtk.ResponseType.NO:
            respNO()
        dialog.destroy()


class MessageError:
    def msg_error(self, txt_prin, txt_sec):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=txt_prin,
        )
        dialog.format_secondary_text(
            txt_sec
        )
        dialog.run()
        dialog.destroy()


class MessageWarning:

    def msg_warning_continue(self, txt_prin, txt_sec):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK,
            text=txt_prin,
        )
        dialog.format_secondary_text(
            txt_sec
        )
        dialog.run()
        dialog.destroy()

    def msg_warning_ok_cancel(self, txt_prin, txt_sec, respYES, respNO):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.YES_NO,
            text=txt_prin,
        )
        dialog.format_secondary_text(
            txt_sec
        )
        respuesta = dialog.run()
        if respuesta == Gtk.ResponseType.YES:
            respYES()
        elif respuesta == Gtk.ResponseType.NO:
            respNO()
        dialog.destroy()
