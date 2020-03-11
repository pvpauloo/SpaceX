import process
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button


Window.clearcolor = .50, .50, .92, 1
Builder.load_file('kvlang.kv')
cap = []


class TelaInicial(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self.soltou)

    def interageNaTela(self, texto):
        label = self.ids.mensagem
        label.text = texto

    def soltou(self, window, caminho_arquivo):
        cap.append(caminho_arquivo.decode('utf-8'))
        self.interageNaTela(f'Arquivos processados, abaixo os desfazimentos')
        pc = process.ModuloProcessamento.geral(self, cap)
        process.ModuloProcessamento.newexcel(self, pc)
        self.ids.area_resultado.add_widget(Button(text='Data', size_hint_y=None, font_size=15, height=15))
        self.ids.area_resultado.add_widget(Button(text='MTI', size_hint_y=None, font_size=15, height=15))
        self.ids.area_resultado.add_widget(Button(text='Card Number', size_hint_y=None, font_size=15, height=15))
        self.ids.area_resultado.add_widget(Button(text='Processing Code', size_hint_y=None, font_size=15, height=15))
        self.ids.area_resultado.add_widget(Button(text='Terminal Code', size_hint_y=None, font_size=15, height=15))
        self.ids.area_resultado.add_widget(Button(text='Response Code', size_hint_y=None, font_size=15, height=15))
        for item in pc:
            if item['MTI'].__contains__('0420'):
                self.ids.area_resultado.add_widget(Label(text=item['Data'], color=(.47, .47, .47, 1), size_hint_y=None, font_size=15, height=15))
                self.ids.area_resultado.add_widget(Label(text=item['MTI'], color=(.47, .47, .47, 1), size_hint_y=None, font_size=15, height=15))
                self.ids.area_resultado.add_widget(Label(text=item['Card Number'], color=(.47, .47, .47, 1), size_hint_y=None, font_size=15, height=15))
                self.ids.area_resultado.add_widget(Label(text=item['Processing Code'], color=(.47, .47, .47, 1), size_hint_y=None, font_size=15, height=15))
                self.ids.area_resultado.add_widget(Label(text=item['Terminal Code'], color=(.47, .47, .47, 1), size_hint_y=None, font_size=15, height=15))
                self.ids.area_resultado.add_widget(Label(text=item['Response Code'], color=(.47, .47, .47, 1), size_hint_y=None, font_size=15, height=15))



sm = ScreenManager()
tela = TelaInicial(name='tela_inicial')
sm.add_widget(tela)


class Programa(App):
    title = 'Converte Q2'

    def build(self):
        return sm


if __name__ == '__main__':
    start = Programa()
    start.run()

