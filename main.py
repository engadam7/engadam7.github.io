from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text="Ku soo dhawow App-kaaga!", font_size='24sp')
        btn = Button(text="I Taabo!", size_hint=(1, 0.3), background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.label.text = "Waad ku guuleysatay! APK-gu wuu shaqeynayaa."

if __name__ == '__main__':
    MyApp().run()

