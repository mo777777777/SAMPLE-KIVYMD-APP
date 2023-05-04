import kivy
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen




l=['blue','yellow','cyan','green','pink','red','gray','orange','gold','purple','coral','lime','olive','teal','bisque','magenta']
color=random.choice(l)
Window.clearcolor=(color)
Window.size=(400,630)





class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class LoginWindow(Screen):
    pass


class ErrorWindow(Screen):
    pass

class VidowWindow(Screen):
    pass

class PdfWindow(Screen):
    pass

class QuestionWindow(Screen):
    pass

class Comingsoon(Screen):
    pass


kv=Builder.load_file('main.kv')
class MyMainApp(App):
    def build(self):
        self.title='mohamed'
        self.icon='Y.png'
        return kv 
    
    
    
    
    
if __name__=='__main__':
    MyMainApp().run()