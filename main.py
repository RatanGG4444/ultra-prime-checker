from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Set background color to dark charcoal
Window.clearcolor = (0.12, 0.12, 0.12, 1)

def get_factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

class PrimeApp(App):
    def build(self):
        self.title = "Ultra Prime Checker"
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Display Box
        self.display = Label(
            text="", 
            font_size='36sp', 
            size_hint_y=0.2, 
            halign='right', 
            valign='middle',
            color=(1, 1, 1, 1)
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)
        
        # Result Labels
        self.result_label = Label(
            text="Enter a number & press CHECK", 
            font_size='16sp', 
            size_hint_y=0.1,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.result_label)
        
        self.factors_label = Label(
            text="", 
            font_size='14sp', 
            size_hint_y=0.1,
            color=(0.7, 0.7, 0.8, 1)
        )
        main_layout.add_widget(self.factors_label)
        
        # Keypad Grid
        keypad = GridLayout(cols=3, spacing=8, size_hint_y=0.6)
        
        # Row 0
        btn_c = Button(text="C", font_size='20sp', background_color=(0.9, 0.2, 0.2, 1))
        btn_c.bind(on_press=self.clear_display)
        
        btn_back = Button(text="⌫", font_size='20sp', background_color=(1, 0.7, 0, 1))
        btn_back.bind(on_press=self.backspace)
        
        btn_check = Button(text="CHECK", font_size='18sp', background_color=(0, 0.5, 0.9, 1))
        btn_check.bind(on_press=self.check_number)
        
        keypad.add_widget(btn_c)
        keypad.add_widget(btn_back)
        keypad.add_widget(btn_check)
        
        # Numbers 1-9
        for num in ['7', '8', '9', '4', '5', '6', '1', '2', '3']:
            btn = Button(text=num, font_size='22sp', background_color=(0.2, 0.2, 0.2, 1))
            btn.bind(on_press=lambda instance, n=num: self.add_digit(n))
            keypad.add_widget(btn)
            
        # Zero Button
        btn_zero = Button(text="0", font_size='22sp', background_color=(0.2, 0.2, 0.2, 1))
        btn_zero.bind(on_press=lambda instance: self.add_digit("0"))
        
        # Add padding spaces for grid layout
        keypad.add_widget(Label())
        keypad.add_widget(btn_zero)
        keypad.add_widget(Label())
        
        main_layout.add_widget(keypad)
        return main_layout

    def add_digit(self, char):
        if len(self.display.text) < 10:
            self.display.text += char

    def clear_display(self):
        self.display.text = ""
        self.result_label.text = "Enter a number & press CHECK"
        self.result_label.color = (1, 1, 1, 1)
        self.factors_label.text = ""

    def backspace(self, instance):
        self.display.text = self.display.text[:-1]

    def check_number(self, instance):
        text = self.display.text.strip()
        if not text:
            self.result_label.text = "Please enter a number!"
            return

        n = int(text)
        if n <= 0:
            self.result_label.text = "Enter positive numbers only!"
            return

        factors = get_factors(n)
        if len(factors) == 2:
            self.result_label.text = f"✨ {n} IS A PRIME NUMBER! ✨"
            self.result_label.color = (0.3, 0.9, 0.4, 1)
        else:
            self.result_label.text = f"❌ {n} IS NOT A PRIME NUMBER"
            self.result_label.color = (0.9, 0.3, 0.4, 1)

        self.factors_label.text = "Factors: " + ", ".join(map(str, factors))

if __name__ == "__main__":
    PrimeApp().run()