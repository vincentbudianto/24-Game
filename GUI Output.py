''' NIM/Nama  : 13517020/T. Antra Oksidian Tafly, 13517137/Vincent Budianto, 13517146/Hansen
	Nama file : GUI Output.py
	Topik     : Tugas Besar 1 IF2211-Strategi Algoritma
	Tanggal   : 13 Februari 2019
	Deskripsi : GUI untuk output hasil '''

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.button import MDIconButton
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivymd.theming import ThemeManager

main_widget_kv = '''
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDTextField kivymd.textfields.MDTextField
        
<Screen1>:
	BoxLayout:
		orientation: 'vertical'
		padding: dp(48)
		spacing: 10
		MDRaisedButton:
			id: button1
			text: "Show Result"
			elevation_normal: 2
			opposite_colors: True
			pos_hint: {'center_x': 0.5, 'center_y': 0.4}
			on_release: root.out()
			opacity: 1
		BoxLayout:
			MDLabel:
				id: label1
				font_style: 'Display1'
				theme_text_color: 'Primary'
				text: "Hasil :"
				halign: 'center'
				valign: 'top'
				size_hint_y: 0.4
				opacity: 0
		BoxLayout:
			MDLabel:
				id: hasil
				font_style: 'Display2'
				theme_text_color: 'Primary'
				text: ""
				halign: 'center'
				valign: 'top'
				size_hint_y: 2.1
'''
cek = False

class Screen1(Screen):
	def out(self):
		global cek

		if (not cek):
			cek = True
			self.ids.button1.opacity = 0
			self.ids.label1.opacity = 1
			x = 'berhasil'
			self.ids.hasil.text += str(x)

class main(App):
	theme_cls = ThemeManager()
	title = "Output"
	
	def build(self):
		global cek
		main_widget = Builder.load_string(main_widget_kv)
		sm = ScreenManager()
		sm.add_widget(Screen1(name='Screen1'))
		#self.theme_cls.theme_style = 'Dark'

		return sm
	
if __name__ == '__main__':
	main().run()