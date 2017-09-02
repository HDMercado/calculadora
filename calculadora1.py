import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")

        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.operacion=""

        self.label1 = Gtk.Label("")
        self.label2 = Gtk.Label("")
        self.label = Gtk.Label(self.operacion)
        self.b_potencia = Gtk.Button(label="   ^   ")
        self.b_potencia.connect("clicked", self.potencia)
        self.b_borrar = Gtk.Button(label="Borrar")
        self.b_borrar.connect("clicked", self.borrar)
        self.b_dividir = Gtk.Button(label="   /   ")
        self.b_dividir.connect("clicked", self.divide)
        self.b_multiplicar = Gtk.Button(label="   *   ")
        self.b_multiplicar.connect("clicked", self.multiplicar)
        self.b_suma = Gtk.Button(label="   +   ")
        self.b_suma.connect("clicked", self.suma)
        self.b_resta = Gtk.Button(label="   -   ")
        self.b_resta.connect("clicked", self.resta)
        self.b_igual = Gtk.Button(label="    =   ")
        self.b_igual.connect("clicked", self.igual)
        self.b_abierto = Gtk.Button(label="   (   ")
        self.b_abierto.connect("clicked", self.abierto)
        self.b_cerrado = Gtk.Button(label="    )   ")
        self.b_cerrado.connect("clicked", self.cerrado)
        self.b_coma = Gtk.Button(label="   .   ")
        self.b_coma.connect("clicked", self.coma)
        self.b_1 = Gtk.Button(label="   1   ")
        self.b_1.connect("clicked", self.uno)
        self.b_2 = Gtk.Button(label="   2   ")
        self.b_2.connect("clicked", self.dos)
        self.b_3 = Gtk.Button(label="   3   ")
        self.b_3.connect("clicked", self.tres)
        self.b_4 = Gtk.Button(label="   4   ")
        self.b_4.connect("clicked", self.cuatro)
        self.b_5 = Gtk.Button(label="   5   ")
        self.b_5.connect("clicked", self.cinco)
        self.b_6 = Gtk.Button(label="   6   ")
        self.b_6.connect("clicked", self.seis)
        self.b_7 = Gtk.Button(label="   7   ")
        self.b_7.connect("clicked", self.siete)
        self.b_8 = Gtk.Button(label="   8   ")
        self.b_8.connect("clicked", self.ocho)
        self.b_9 = Gtk.Button(label="   9   ")
        self.b_9.connect("clicked", self.nueve)
        self.b_0 = Gtk.Button(label="   0   ")
        self.b_0.connect("clicked", self.cero)
        
        self.grid.attach(self.label1, 0, 0, 4, 1)
        self.grid.attach(self.label, 0, 1, 4, 1)
        self.grid.attach(self.label2, 0, 2, 4, 1)
        self.grid.attach(self.b_potencia, 0, 3, 1, 1)
        self.grid.attach(self.b_abierto, 1, 3, 1, 1)
        self.grid.attach(self.b_cerrado, 2, 3, 1, 1)
        self.grid.attach(self.b_7, 0, 4, 1, 1)
        self.grid.attach(self.b_8, 1, 4, 1, 1)
        self.grid.attach(self.b_9, 2, 4, 1, 1)
        self.grid.attach(self.b_4, 0, 5, 1, 1)
        self.grid.attach(self.b_5, 1, 5, 1, 1)
        self.grid.attach(self.b_6, 2, 5, 1, 1)
        self.grid.attach(self.b_1, 0, 6, 1, 1)
        self.grid.attach(self.b_2, 1, 6, 1, 1)
        self.grid.attach(self.b_3, 2, 6, 1, 1)
        self.grid.attach(self.b_borrar, 0, 7, 1, 1)
        self.grid.attach(self.b_0, 1, 7, 1, 1)
        self.grid.attach(self.b_coma, 2, 7, 1, 1)
        self.grid.attach(self.b_dividir, 3, 3, 1, 1)
        self.grid.attach(self.b_multiplicar, 3, 4, 1, 1)
        self.grid.attach(self.b_resta, 3, 5, 1, 1)
        self.grid.attach(self.b_suma, 3, 6, 1, 1)
        self.grid.attach(self.b_igual, 3, 7, 1, 1)

    def potencia(self, widgetd):
        x="**"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def divide(self, widgetd):
        x="/"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def multiplicar(self, widget):
        x="*"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def suma(self, widget):
        x="+"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def resta(self, widget):
        x="-"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def coma(self, widget):
        x="."
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def igual(self, widget):
        x=str(eval(self.operacion))
        self.label.set_text(x)
    def borrar(self, widget):
        self.operacion=""
        self.label.set_text(self.operacion)
    def abierto(self, widget):
        x="("
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def cerrado(self, widget):
        x=")"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def uno(self, widget):
        x="1"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def dos(self, widget):
        x="2"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def tres(self, widget):
        x="3"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def cuatro(self, widget):
        x="4"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def cinco(self, widget):
        x="5"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def seis(self, widget):
        x="6"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def siete(self, widget):
        x="7"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def ocho(self, widget):
        x="8"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def nueve(self, widget):
        x="9"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)
    def cero(self, widget):
        x="0"
        self.operacion=self.operacion+x
        self.label.set_text(self.operacion)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

