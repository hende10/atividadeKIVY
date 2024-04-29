from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage (source = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTudDGHI3iwXjDImpjoJSoerf4O_ZzJfhG5svOIBrT_Lg&s')
    
if __name__ == '__main__':
    MinhaApp().run()