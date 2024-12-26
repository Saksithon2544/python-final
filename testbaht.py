import tkinter as tk
from tkinter import messagebox

def number_to_words(n):
    ones = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]

    def convert_integer(num):
        """ แปลงจำนวนเต็มเป็นคำอ่าน """
        if num == 0:
            return ""
        elif num == 1:
            return "หนึ่ง"
        elif num < 10:
            return ones[num]
        elif num < 100:
            if num == 10:
                return "สิบ"
            elif num % 10 == 1:
                return tens[num // 10] + "เอ็ด"
            return tens[num // 10] + ones[num % 10]
        elif num < 1000:
            if num // 100 == 1:
                return "หนึ่งร้อย" + convert_integer(num % 100)
            return ones[num // 100] + "ร้อย" + convert_integer(num % 100)
        elif num < 10000:
            if num // 1000 == 1:
                return "หนึ่งพัน" + convert_integer(num % 1000)
            return ones[num // 1000] + "พัน" + convert_integer(num % 1000)
        elif num < 100000:
            return convert_integer(num // 10000) + "หมื่น" + convert_integer(num % 10000)
        elif num < 1000000:
            return convert_integer(num // 100000) + "แสน" + convert_integer(num % 100000)
        else:
            return convert_integer(num // 1000000) + "ล้าน" + convert_integer(num % 1000000)

    def convert_decimal(num):
        """ แปลงส่วนทศนิยมเป็นคำอ่าน """
        if num == 0:
            return ""
        return convert_integer(num)

    integer_part = int(n)
    decimal_part = int(round(n - integer_part, 2) * 100)

    integer_words = convert_integer(integer_part) + "บาท"
    if decimal_part == 0:
        return integer_words + "ถ้วน"
    else:
        decimal_words = convert_decimal(decimal_part) + "สตางค์"
        return integer_words + decimal_words

def convert():
    try:
        number_str = entry.get().strip()
        if not number_str:
            raise ValueError("กรุณากรอกตัวเลข")

        number = float(number_str)
        if number < 0:
            raise ValueError("กรุณากรอกตัวเลขที่มากกว่าหรือเท่ากับศูนย์")

        result = number_to_words(number)
        result_label.config(text=f"ผลลัพธ์: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("แปลงตัวเลขเป็นคำ")

# สร้าง label สำหรับคำแนะนำ
instruction_label = tk.Label(root, text="กรุณากรอกจำนวนเงินที่ต้องการแปลง (ไม่เกิน 2 ตำแหน่งทศนิยม)")
instruction_label.pack(pady=10)

# สร้าง Textbox สำหรับกรอกตัวเลข
entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.pack(pady=10)

# สร้างปุ่มสำหรับแปลงตัวเลข
convert_button = tk.Button(root, text="แปลง", font=("Arial", 14), command=convert)
convert_button.pack(pady=10)

# สร้าง label สำหรับแสดงผลลัพธ์
result_label = tk.Label(root, text="ผลลัพธ์: ", font=("Arial", 14))
result_label.pack(pady=10)

# เริ่มต้น loop ของ GUI
root.mainloop()
