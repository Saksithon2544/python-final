import tkinter as tk
from tkinter import ttk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("เครื่องคิดเลข")
        self.current_input = ""
        self.create_widgets()
        self.root.bind("<Key>", self.on_key_press)

    def create_widgets(self):
        # Style for buttons and labels
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 18), padding=5)
        style.configure("TLabel", font=("Arial", 24), padding=10)

        # Display result
        self.result_label = ttk.Label(self.root, text="", anchor="e", background="white", relief="sunken")
        self.result_label.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=10)

        # Buttons configuration
        buttons = [
            ("(", 1, 0, 1), (")", 1, 1, 1), ("C", 1, 2, 1), ("CE", 1, 3, 1),
            ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("/", 2, 3, 1),
            ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("*", 3, 3, 1),
            ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("-", 4, 3, 1),
            ("0", 5, 0, 1), (".", 5, 1, 1), ("=", 5, 2, 1), ("+", 5, 3, 1),
            ("%", 6, 0, 1), ("√", 6, 1, 1), ("ปิด", 6, 2, 2),
        ]

        for text, row, col, colspan in buttons:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="we", padx=5, pady=5)
    
    def on_button_click(self, button_text):
        if button_text == "=":
            self.evaluate_expression()
        elif button_text == "C":
            self.clear()
        elif button_text == "CE":
            self.current_input = self.current_input[:-1]
            self.result_label.config(text=self.current_input)
        elif button_text == "√":
            self.calculate_square_root()
        elif button_text == "%":
            self.calculate_percentage()
        elif button_text == "ปิด":
            self.close()
        elif button_text == ".":
            # Check if the last number already contains a "."
            last_number = self.current_input.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
            if "." not in last_number:
                self.current_input += button_text
                self.result_label.config(text=self.current_input)
        else:
            self.current_input += button_text
            self.result_label.config(text=self.current_input)


    def on_key_press(self, event):
        key = event.char
        valid_keys = "0123456789.+-*/()%"
        if key in valid_keys:
            self.on_button_click(key)
        elif event.keysym == "Return":
            self.on_button_click("=")
        elif event.keysym == "BackSpace":
            self.on_button_click("CE")
        elif event.keysym == "Escape":
            self.clear()
        elif event.keysym.lower() == "q":
            self.close()

    def evaluate_expression(self):
        try:
            # Safe evaluation
            result = eval(self.current_input, {"__builtins__": None}, {"math": math})
            if isinstance(result, (int, float)):
                self.result_label.config(text=str(result))
                self.current_input = str(result)
            else:
                raise ValueError
        except ZeroDivisionError:
            self.result_label.config(text="หารด้วยศูนย์ไม่ได้")
            self.current_input = ""
        except Exception:
            self.result_label.config(text="ข้อผิดพลาด")
            self.current_input = ""

    def calculate_square_root(self):
        try:
            number = float(self.current_input)
            if number < 0:
                raise ValueError
            result = math.sqrt(number)
            self.result_label.config(text=str(result))
            self.current_input = str(result)
        except Exception:
            self.result_label.config(text="ข้อผิดพลาด")
            self.current_input = ""

    def calculate_percentage(self):
        try:
            result = float(self.current_input) / 100
            print(result)
            self.result_label.config(text=str(result))
            self.current_input = str(result)
        except Exception:
            self.result_label.config(text="ข้อผิดพลาด")
            self.current_input = ""

    def clear(self):
        self.current_input = ""
        self.result_label.config(text="")

    def close(self):
        self.root.quit()
        self.root.destroy()

# Start application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
