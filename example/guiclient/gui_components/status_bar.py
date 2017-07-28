from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class StaturBar(BoxLayout):
  def __init__(self, on_connect_callback, **kwargs):
    super(StaturBar, self).__init__(**kwargs)
    self._on_connect_callback = on_connect_callback
    self.build()

  def build(self):
    self.ip_address_input = TextInput(text='127.0.0.1')
    self.port_input = TextInput(text='5555')
    self.launch_label = Label(text='Launch Environment', halign='right', font_size=12)
    self.launch_check_box = CheckBox(active=True)
    self.connect_button = Button(text='Connect')
    self.connect_button.bind(on_release=self.on_connect_button)

    self.add_widget(self.ip_address_input)
    self.add_widget(self.port_input)
    self.add_widget(self.launch_label)
    self.add_widget(self.launch_check_box)
    self.add_widget(self.connect_button)
    return self

  def on_connect_button(self, value):
    self._on_connect_callback(self.ip_address_input.text, self.port_input.text, self.launch_check_box.active)

  def update_connect_button(self, value: str):
    self.connect_button.text = value
    if (value == 'Disconnect'):
      self.launch_check_box.disabled = True
      self.ip_address_input.disabled = True
      self.port_input.disabled = True
    else:
      self.launch_check_box.disabled = False
      self.ip_address_input.disabled = False
      self.port_input.disabled = False
