import kivy
from kivy.app import App
from kivy.uix.label import Label

# Minimum version requirement for Kivy
kivy.require('2.0.0')

class MyApp(App):
    def build(self):
        # Create a Label widget with some text
        return Label(text='Hello from Kivy!')

if __name__ == '__main__':
    # Run the Kivy application
    MyApp().run()
