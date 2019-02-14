''' NIM/Nama  : 13517020/T. Antra Oksidian Tafly, 13517137/Vincent Budianto, 13517146/Hansen
	Nama file : GUI Output.py
	Topik     : Tugas Besar 1 IF2211-Strategi Algoritma
	Tanggal   : 13 Februari 2019
	Deskripsi : GUI untuk output hasil '''

import time
from functions import *
from kivy.core.window import Window
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.image import Image
from kivymd.button import MDIconButton
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.animation import Animation
from kivymd.theming import ThemeManager

main_widget_kv = '''
#:import hex kivy.utils.get_color_from_hex
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDTextField kivymd.textfields.MDTextField
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManager:
	id: scr_mngr
	transition: FadeTransition()
	Screen1:
		name: 'Screen1'
		canvas.before:
			Rectangle:
				source:'./Picture/gbr.jpg'
				pos: self.pos
				size: self.size
		MDLabel:
			id: title1
			font_style: 'Display1'
			text: "                             #####    #                 #            #   ##########   ########                      #"
			halign: 'left'
			size_hint_y: 1.8
			opacity: 1
		MDLabel:
			id: title2
			font_style: 'Display1'
			text: "                            #         #   #        #          #       #                     ###                        #   ##########"
			halign: 'left'
			size_hint_y: 1.7
			opacity: 1
		MDLabel:
			id: title3
			font_style: 'Display1'
			text: "                                       #   #        #       #   #   #                     #                            #                     ##"
			halign: 'left'
			size_hint_y: 1.6
			opacity: 1
		MDLabel:
			id: title4
			font_style: 'Display1'
			text: "                             ####    #        #                #                      #                         ##                   ##  #"
			halign: 'left'
			size_hint_y: 1.5
			opacity: 1
		MDLabel:
			id: title5
			font_style: 'Display1'
			text: "                            #            ######            #  #                 #                      ##   #               ##       #"
			halign: 'left'
			size_hint_y: 1.4
			opacity: 1
		MDLabel:
			id: title6
			font_style: 'Display1'
			text: "                            #                      #             #      #             #                      ##       #         ##        ##  "
			halign: 'left'
			size_hint_y: 1.3
			opacity: 1
		MDLabel:
			id: title7
			font_style: 'Display1'
			text: "                            #####           #                        #         #                      #              #                       #  "
			halign: 'left'
			size_hint_y: 1.2
			opacity: 1
		BoxLayout:
			orientation: 'vertical'
			size_hint_y: 0.4
			height: dp(225)
			padding: dp(48)
			spacing: 15
			BoxLayout:
				orientation: 'vertical'
				MDTextField:
					id: playername
					hint_text: "Player's Name"
					max_text_length: 10
				MDLabel:
					id: errorcode
					theme_text_color: 'Error'
					text: "Player's name is more than 10 characters"
					halign: 'center'
					valign: 'top'
					opacity: 0
			BoxLayout:
				orientation: 'horizontal'
				Button:
					id: button1
					text: "START"
					background_color: hex('#33ff33')
					size_hint: 0.1, 0.5
					elevation_normal: 2
					opposite_colors: True
					pos_hint: {'center_x': 0.5, 'center_y': 0.4}
					on_press:
						app.valid()
						pname1.text = "Name : " + playername.text
						cardsleft1.text = "Cards Left: " + _cardsleft.text
						pname2.text = "Name : " + playername.text
						cardsleft2.text = "Cards Left: " + _cardsleft.text
				Button:
					id: button2
					text: "EXIT"
					background_color: hex('#FF0000')
					size_hint: 0.1, 0.5
					elevation_normal: 2
					opposite_colors: True
					pos_hint: {'center_x': 0.5, 'center_y': 0.4}
					on_press:
						app.close()
	

	Screen2:
		name: 'Screen2'
		id: Screen2
		canvas.before:
			Color:
				rgba: 0, 1, 1, 1
			Rectangle:
				source: './Picture/gbr2.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			MDLabel:
				id: label1
				font_style: 'Display3'
				color: hex('#FFEFD5')
				text: "24 GAME"
				bold: True
				halign: 'center'
				valign: 'top'
				size_hint_y: 1.8
		BoxLayout:
			padding: dp(48)
			orientation: 'vertical'
			MDLabel:
				id: _hasil
				text: ''
				opacity: 0

			MDLabel:
				id: _poin
				text: ''
				opacity: 0
			MDLabel:
				id: _cardsleft
				text: ''
				opacity: 0
			Button:
				id: button3
				text: "NEXT"
				background_color: hex('#80ffff')
				size_hint: 0.1, 0.5
				elevation_normal: 2
				opposite_colors: True
				pos_hint: {'center_x': 0.5, 'center_y': 0.4}
				on_press:
					app.next()
					hasil.text = _hasil.text
					poin.text = _poin.text
					cardsleft1.text = "Cards Left: " + _cardsleft.text
					cardsleft2.text = "Cards Left: " + _cardsleft.text
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: 0.3
			pos: -500, 400
			Image:
				id: gbr1
				source: ''
			Image:
				id: gbr2
				source: ''
			Image:
				id: gbr3
				source: ''
			Image:
				id: gbr4
				source: ''
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: None
			height: self.minimum_height
			padding: dp(20)
			spacing: 50
			MDLabel:
				id: pname1
				font_style: 'Subhead'
				color: hex('#FFEFD5')
				text: ""
				halign: 'left'
				valign: 'bottom'
			MDLabel:
				id: cardsleft1
				font_style: 'Subhead'
				color: hex('#FFEFD5')
				text: ""
				halign: 'right'
				valign: 'bottom'

	Screen3:
		name: 'Screen3'
		id: Screen3
		canvas.before:
			Color:
				rgba: 0, 1, 1, 1
			Rectangle:
				source:'./Picture/gbr3.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			MDLabel:
				id: label2
				font_style: 'Display3'
				color: hex('#FFEFD5')
				text: "24 GAME"
				bold: True
				halign: 'center'
				valign: 'top'
				size_hint_y: 1.8
		BoxLayout:
			orientation: 'vertical'
			size_hint_y: 0.35
			pos: -75, 275
			spacing: 50
			BoxLayout:
				orientation: 'horizontal'
				size_hint_y: 0.35
				center: self.parent.center
				padding: dp(48)
				spacing: 50
				BoxLayout:
					orientation: 'vertical'
					MDLabel:
						id: label3
						font_style: 'Display1'
						color: hex('#FFEFD5')
						text: "Hasil       : "
						halign: 'right'
						valign: 'top'
						opacity: 0
					MDLabel:
						id: label4
						font_style: 'Display1'
						color: hex('#FFEFD5')
						text: "Poin        : "
						halign: 'right'
						valign: 'top'
						opacity: 0
					MDLabel:
						id: label5
						font_style: 'Display1'
						color: hex('#FFEFD5')
						text: "Total Poin  : "
						halign: 'right'
						valign: 'top'
						opacity: 0
				BoxLayout:
					orientation: 'vertical'
					MDLabel:
						id: hasil
						font_style: 'Display2'
						color: hex('#FFEFD5')
						text: ""
						halign: 'left'
						valign: 'top'
						opacity: 0
					MDLabel:
						id: poin
						font_style: 'Display2'
						color: hex('#FFEFD5')
						text: ""
						halign: 'left'
						valign: 'top'
						opacity: 0
					MDLabel:
						id: totalpoin
						font_style: 'Display2'
						color: hex('#FFEFD5')
						text: "0"
						halign: 'left'
						valign: 'top'
						opacity: 0
				BoxLayout:
					orientation: 'vertical'
					spacing: 50
					BoxLayout:
						Button:
							id: button4
							text: "NEXT DRAW"
							background_color: hex('#80ffff')
							size_hint: 0.3, 1.5
							elevation_normal: 2
							opposite_colors: True
							pos_hint: {'center_x': 0.5, 'center_y': 0.4}
							on_press:
								app.nextdraw()
					BoxLayout:
						Button:
							id: button5
							text: "NEW GAME"
							background_color: hex('#33ff33')
							size_hint: 0.3, 1.5
							elevation_normal: 2
							opposite_colors: True
							pos_hint: {'center_x': 0.5, 'center_y': 0.4}
							on_press:
								hasil.text = ""
								_hasil.text = ""
								poin.text = ""
								_poin.text = ""
								totalpoin.text = "0"
								pname1.text = "Name : "
								pname2.text = "Name : "
								playername.text = ""
								cardsleft1.text = "Cards Left: "
								cardsleft2.text = "Cards Left: "
								_cardsleft.text = ""
								root.current = 'Screen1'
								app.newgame()
					BoxLayout:
						Button:
							id: button6
							text: "EXIT"
							background_color: hex('#FF0000')
							size_hint: 0.3, 1.5
							elevation_normal: 2
							opposite_colors: True
							pos_hint: {'center_x': 0.5, 'center_y': 0.4}
							on_release:
								app.close()
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: None
			height: self.minimum_height
			padding: dp(20)
			spacing: 50
			MDLabel:
				id: pname2
				font_style: 'Subhead'
				color: hex('#FFEFD5')
				text: ""
				halign: 'left'
				valign: 'bottom'
			MDLabel:
				id: cardsleft2
				font_style: 'Subhead'
				color: hex('#FFEFD5')
				text: ""
				halign: 'right'
				valign: 'bottom'
'''

deck = initiatedeck()

class Screen1(Screen):
	pass

class Screen2(Screen):
	pass

class Screen3(Screen):
	pass

class main(App):
	theme_cls = ThemeManager()
	title = "24 Game"
	Window.fullscreen = 'auto'

	def build(self):
		main_widget = Builder.load_string(main_widget_kv)
		return main_widget
        
	def valid(self):
		global deck
		global List

		if (len(self.root.ids.playername.text) <= 10):
			self.root.ids.errorcode.opacity = 0
			self.root.ids._cardsleft.text = str(len(deck))
			(List, deck, drawncards) = draw4(deck)
			self.root.ids.gbr1.source = str(drawncards[0].FN)
			self.root.ids.gbr2.source = str(drawncards[1].FN)
			self.root.ids.gbr3.source = str(drawncards[2].FN)
			self.root.ids.gbr4.source = str(drawncards[3].FN)
			
			anim1 = Animation(x = 50, y = 400, t = 'linear', duration = 1)
			anim2 = Animation(x = 400, y = 400, t = 'linear', duration = 1)
			anim3 = Animation(x = 750, y = 400, t = 'linear', duration = 1)
			anim4 = Animation(x = 1100, y = 400, t = 'linear', duration = 1)
			anim1.start(self.root.ids.gbr1)
			anim2.start(self.root.ids.gbr2)
			anim3.start(self.root.ids.gbr3)
			anim4.start(self.root.ids.gbr4)
			
			reset1 = Animation(opacity = 0)
			reset1.start(self.root.ids.title1)
			reset1.start(self.root.ids.title2)
			reset1.start(self.root.ids.title3)
			reset1.start(self.root.ids.title4)
			reset1.start(self.root.ids.title5)
			reset1.start(self.root.ids.title6)
			reset1.start(self.root.ids.title7)
			
			self.root.current = 'Screen2'
		else:
			self.root.ids.errorcode.opacity = 1

	def next(self):
		global List

		totalscore=0
		(List,totalscore)=Listprocessf(List,totalscore)
		(List[0].E,totalscore)=kurung(List[0].E,totalscore)
		totalscore-=abs(24-List[0].N)
		
		reset2 = Animation(x = -500, y = 400, t = 'linear', duration = 2)
		reset2.start(self.root.ids.gbr1)
		reset2.start(self.root.ids.gbr2)
		reset2.start(self.root.ids.gbr3)
		reset2.start(self.root.ids.gbr4)
		
		self.root.ids._hasil.text = str(List[0].E)
		self.root.ids._poin.text = str(totalscore)
		self.root.ids._cardsleft.text = str(len(deck))
		self.root.ids.totalpoin.text = str(int(self.root.ids.totalpoin.text) + int(self.root.ids._poin.text))

		animat = Animation(opacity = 1, duration = 1)
		animat.start(self.root.ids.label3)
		animat.start(self.root.ids.hasil)
		animat.start(self.root.ids.label4)
		animat.start(self.root.ids.poin)
		animat.start(self.root.ids.label5)
		animat.start(self.root.ids.totalpoin)
		
		self.root.current = 'Screen3'

	def nextdraw(self):
		global deck
		global List


		if (len(deck) > 0):
			(List, deck, drawncards) = draw4(deck)
			self.root.ids.gbr1.source = str(drawncards[0].FN)
			self.root.ids.gbr2.source = str(drawncards[1].FN)
			self.root.ids.gbr3.source = str(drawncards[2].FN)
			self.root.ids.gbr4.source = str(drawncards[3].FN)
			
			anim1 = Animation(x = 50, y = 400, t = 'linear', duration = 1)
			anim2 = Animation(x = 400, y = 400, t = 'linear', duration = 1)
			anim3 = Animation(x = 750, y = 400, t = 'linear', duration = 1)
			anim4 = Animation(x = 1100, y = 400, t = 'linear', duration = 1)
			anim1.start(self.root.ids.gbr1)
			anim2.start(self.root.ids.gbr2)
			anim3.start(self.root.ids.gbr3)
			anim4.start(self.root.ids.gbr4)
			
			reset3 = Animation(opacity = 0)
			reset3.start(self.root.ids.label3)
			reset3.start(self.root.ids.hasil)
			reset3.start(self.root.ids.label4)
			reset3.start(self.root.ids.poin)
			reset3.start(self.root.ids.label5)
			reset3.start(self.root.ids.totalpoin)
			
			self.root.current = 'Screen2'
		else:
			content = MDLabel(font_style = 'Body1',
							  theme_text_color = 'Secondary',
							  text = "There's no card left. The game is over!\n"
									 "Please start a new game or exit the game.",
							  size_hint_y = None,
							  valign = 'top')
			content.bind(texture_size = content.setter('size'))
			self.dialog = MDDialog(title = "GAME OVER",
								   content = content,
								   size_hint = (.8, None),
								   height = dp(200),
								   auto_dismiss = False)

			self.dialog.add_action_button("Dismiss",
										  action=lambda *x: self.dialog.dismiss())
			self.dialog.open()

	def	newgame(self):
		global deck

		deck = initiatedeck()
		
		reset4 = Animation(opacity = 0)
		reset4.start(self.root.ids.label4)
		reset4.start(self.root.ids.hasil)
		reset4.start(self.root.ids.label4)
		reset4.start(self.root.ids.poin)
		reset4.start(self.root.ids.label5)
		reset4.start(self.root.ids.totalpoin)
		
		anima1 = Animation(opacity = 1, duration = 4)
		anima2 = Animation(opacity = 1, duration = 4.5)
		anima3 = Animation(opacity = 1, duration = 5)
		anima4 = Animation(opacity = 1, duration = 5.5)
		anima5 = Animation(opacity = 1, duration = 6)
		anima6 = Animation(opacity = 1, duration = 6.5)
		anima7 = Animation(opacity = 1, duration = 7)
		anima1.start(self.root.ids.title1)
		anima2.start(self.root.ids.title2)
		anima3.start(self.root.ids.title3)
		anima4.start(self.root.ids.title4)
		anima5.start(self.root.ids.title5)
		anima6.start(self.root.ids.title6)
		anima7.start(self.root.ids.title7)

if __name__ == '__main__':
	sound = SoundLoader.load('./Voyage.wav')
	sound.volume = 0.4
	sound.loop = True
	sound.play()
	main().run()
	
