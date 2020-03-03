from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from process import ModuloProcessamento


arquivos = []


class TestApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self.soltou)

    def soltou(self, window, caminho_arquivo):
        arquivos.append(caminho_arquivo.decode('utf-8'))

        ModuloProcessamento.Geral('self', True, arquivos)

    def build(self):
        return Button(text='Hello World')


TestApp().run()

