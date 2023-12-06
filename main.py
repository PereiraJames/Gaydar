import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.clock import Clock
import time
import random

kivy.require('1.9.0')

class MyRoot(BoxLayout):
    background_color = ListProperty([1, 1, 1, 1])
        
    def setDefault(self,dt):
        self.startFlash('stop')
        self.status.text = "AIM AT GAY"
        self.background_color = [1,1,1,1]

    def start_press(self):
        self.start_time = time.time()
        self.status.text = "DETECTING!"
        self.background_color = [1,1,1,1]
        self.startFlash('stop')

    def displayGay(self):
        level = self.detectGay()

        def displayResult(dt):
            if level == 1:
                    self.status.text = "GAY DETECTED!"
                    self.play_sound("CalmGay.mp3")
                    self.startFlash('start')
            elif level == 2:
                self.status.text = "100% GAY"
                self.play_sound("AngryGay.mp3")
                self.startFlash('start')
            elif level == 3:
                self.status.text = "GAY NOT DETECED!"
            else:
                self.status.text = "ERRORRR"
            
            Clock.schedule_once(self.setDefault, 5)

        Clock.schedule_once(displayResult, 3)

    
    def flash_background(self, dt):
        if self.background_color == [1, 1, 1, 1]:  # If current color is red, change to green
            self.background_color = [1, 1, 1, 0.7]
        else:  # Otherwise, change to red
            self.background_color = [1, 1, 1, 1]
    
    def startFlash(self, state):
        if state == "stop":
            Clock.unschedule(self.flash_background)
        elif state == 'start':
            Clock.schedule_interval(self.flash_background, 0.2)

    def detectGay(self):
        releasedTime = time.time() - self.start_time

        if releasedTime < 0.2:
            result = random.randint(0, 3)
            if result != 0:
                return 1
            else:
                return 3
        elif releasedTime > 0.2 and releasedTime < 2:
            return 2
        else:
            return 3

    def play_sound(self, sound_path):
        if hasattr(self, 'currentSound') and self.currentSound and self.currentSound.state == 'play':
            self.currentSound.stop()
        self.currentSound = SoundLoader.load(sound_path)
        if self.currentSound:
            self.currentSound.play()

class GayDar(App):
    def build(self):
        return MyRoot()

gaydar = GayDar()
gaydar.run()
