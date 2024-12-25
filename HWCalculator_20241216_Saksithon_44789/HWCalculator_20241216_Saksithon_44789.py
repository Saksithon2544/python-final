import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("เครื่องคิดเลข")
        self.current_input = ""
        self.create_widgets()
        self.root.bind("<Key>", self.on_key_press)

    def create_widgets(self):
        # แสดงผลลัพธ์
        self.result_label = tk.Label(self.root, text="", height=2, anchor="e", font=("Arial", 24))
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # สร้างปุ่มตัวเลขและเครื่องหมาย
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        # ปุ่มลบเคลียร์ค่า
        clear_button = tk.Button(self.root, text="C", width=5, height=2, font=("Arial", 18), command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # ปุ่มสำหรับปิด
        quit_button = tk.Button(self.root, text="ปิด", width=5, height=2, font=("Arial", 18), command=self.close)
        quit_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                # คำนวณผลลัพธ์
                result = eval(self.current_input)
                self.result_label.config(text=str(result))
                self.current_input = str(result)
            except Exception as e:
                self.result_label.config(text="ข้อผิดพลาด")
                self.current_input = ""
        else:
            # ลบเลข 0 ที่อยู่ข้างหน้าก่อนแสดง
            if self.current_input == "0" and button_text.isdigit():
                self.current_input = button_text
            else:
                self.current_input += button_text
            self.result_label.config(text=self.current_input)

    def on_key_press(self, event):
        key = event.keysym  # ใช้ keysym เพื่อรองรับการกดคีย์ที่หลากหลาย
        if key in "0123456789":  # ตัวเลข 0-9
            self.on_button_click(key)
        elif key in "+-*/":  # เครื่องหมายคำนวณ
            self.on_button_click(key)
        elif key == "Return" or key == "KP_Enter":  # ปุ่ม Enter หรือ Return
            self.on_button_click("=")
        elif key == "BackSpace":  # ลบ
            self.clear()
        elif key == ".":
            if "." not in self.current_input:  # ป้องกันการใส่จุดทศนิยมซ้ำ
                self.on_button_click(key)

    def clear(self):
        self.current_input = ""
        self.result_label.config(text="")
        
    def close(self):
        self.root.quit()
        self.root.destroy()

# เริ่มต้นโปรแกรม
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
