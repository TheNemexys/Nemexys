from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Gli_Indovinelli_Di_Gollum_e_Bilbo(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        Window.size = (360, 640)




        self.window.add_widget(Image(source="logo.png"))



        self.etichetta = Label(
            text="\nSe nella strada vorrai avanzare \nquesti indovinelli dovrai districare, \nhai 5 tentativi.. \no come pegno del tuo fallimento \nla tua vita mi dovrai donare.. \nAccetti la sfida?",
            font_size='20sp',
            color='#007dd1'
             )
        self.window.add_widget(self.etichetta)



        self.input_testo = TextInput(
            size_hint=(1, 0.2),
            font_size='20sp',
            padding_y='12sp',
            halign='center'
            )
        self.window.add_widget(self.input_testo)




        self.bottone = Button(
            text="Invio",
            size_hint=(1, 0.2),
            bold=True,
            background_color='#0099ff'
            )
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press=self.esegui)

        return self.window




    def esegui(self, instance):
        if self.input_testo.text == "si" or self.input_testo.text == "va bene" or self.input_testo.text == "ok":
            self.etichetta.text = "\nPossiamo cominciare.."
        else:
            self.etichetta.text = "\nTorna quando ti saranno \ncresciute le palle.."










Gli_Indovinelli_Di_Gollum_e_Bilbo().run()
