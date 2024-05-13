from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CountApp(App):
    def build(self):
        self.count = 0  # Initialize count
        
        # Layout
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        # Label to display count
        self.count_label = Label(text=str(self.count), font_size=50)
        
        # Text input for setting count
        self.count_input = TextInput(hint_text='Enter Count', multiline=False, input_type='number')

        # Button to set count
        self.set_count_btn = Button(text='Set Count')
        self.set_count_btn.bind(on_press=self.set_count)

        self.layout.add_widget(self.count_label)
        self.layout.add_widget(self.count_input)
        self.layout.add_widget(self.set_count_btn)

        return self.layout

    def set_count(self, instance):
        try:
            new_count = int(self.count_input.text)
            self.count = new_count
            self.count_label.text = str(self.count)
            self.count_input.text = ''  # Clear input field
            self.add_reduce_button()
        except ValueError:
            self.count_label.text = "Invalid input"

    def add_reduce_button(self):
        if not hasattr(self, 'reduce_btn'):
            self.reduce_btn = Button(text='Reduce Count')
            self.reduce_btn.bind(on_press=self.reduce_count)
            self.layout.add_widget(self.reduce_btn)

    def reduce_count(self, instance):
        if self.count > 0:
            self.count -= 1
            self.count_label.text = str(self.count)


if __name__ == '__main__':
    CountApp().run()
