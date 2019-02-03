''' NIM/Nama  : 13517020/T. Antra Oksidian Tafly, 13517137/Vincent Budianto, 13517146/Hansen
	Nama file : GUI Output.py
	Topik     : Tugas Besar 1 IF2211-Strategi Algoritma
	Tanggal   : 13 Februari 2019
	Deskripsi : GUI untuk output hasil '''

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.button import MDIconButton
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivymd.theming import ThemeManager

main_widget_kv = '''
#:import hex kivy.utils.get_color_from_hex
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDTextField kivymd.textfields.MDTextField
        
<Screen1>:
	BoxLayout:
		orientation: 'horizontal'
		canvas.before:
			Rectangle:
				source:'gbr.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			orientation: 'vertical'
			padding: dp(48)
			spacing: 10
			MDRaisedButton:
				id: button1
				text: "START"
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
					text: "Hasil : "
					halign: 'right'
					valign: 'top'
					opacity: 0
					size_hint_y: 0.1
				MDLabel:
					id: hasil
					font_style: 'Display2'
					theme_text_color: 'Primary'
					text: ""
					halign: 'left'
					valign: 'top'
					size_hint_y: 0.1
			BoxLayout:
				MDLabel:
					id: label2
					font_style: 'Display1'
					theme_text_color: 'Primary'
					text: "Poin  : "
					halign: 'right'
					valign: 'top'
					opacity: 0
					size_hint_y: 1.75
				MDLabel:
					id: poin
					font_style: 'Display2'
					theme_text_color: 'Primary'
					text: ""
					halign: 'left'
					valign: 'top'
					size_hint_y: 1.75
'''
cek = False

class Screen1(Screen):
	def out(self):
		global cek

		if (not cek):
			cek = True
			self.ids.button1.opacity = 0
			self.ids.label1.opacity = 1
			self.ids.label2.opacity = 1
			x = '8 * (3 - 8 / 3)'
			y = '8'
			self.ids.hasil.text += str(x)
			self.ids.poin.text += str(y)

class main(App):
	theme_cls = ThemeManager()
	title = "Output"
	
	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		sm = ScreenManager()
		sm.add_widget(Screen1(name='Screen1'))
		self.theme_cls.theme_style = 'Dark'

		return sm
	
if __name__ == '__main__':
	main().run()
