import tkinter as tk
from tkinter import messagebox
import re

def number_to_thai(num):
    units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]
    
    def convert_tens(n, units, tens):
        ten_part = (n % 100) // 10
        parts = []
        if n >= 100:
            parts.append(units[n // 100] + "ร้อย")
            n %= 100
        if n >= 10:
            parts.append(tens[n // 10])
            n %= 10
        if n > 0:
            if n == 1 and ten_part > 0:
                parts.append("เอ็ด")
            elif n == 2 and ten_part > 0:
                parts.append("ยี่")
            else:
                parts.append(units[n])
        return "".join(parts)
    
    def convert_integer_part(n):
        if n == 0:
            return "ศูนย์"
        
        parts = []
        
        if n >= 1000000000000:
            parts.append(convert_tens(n // 1000000000000, units, tens) + "ล้านล้าน")
            n %= 1000000000000
        if n >= 100000000000:
            parts.append(convert_tens(n // 100000000000, units, tens) + "แสนล้าน")
            n %= 100000000000   
        if n >= 10000000000:
            parts.append(convert_tens(n // 10000000000, units, tens) + "หมื่นล้าน")
            n %= 10000000000
        if n >= 1000000000:
            parts.append(convert_tens(n // 1000000000, units, tens) + "พันล้าน")
            n %= 1000000000
        if n >= 100000000:
            parts.append(convert_tens(n // 100000000, units, tens) + "ร้อยล้าน")
            n %= 100000000
        if n >= 10000000:
            parts.append(convert_tens(n // 10000000, units, tens) + "สิบล้าน")
            n %= 10000000
        if n >= 1000000:
            parts.append(convert_tens(n // 1000000, units, tens) + "ล้าน")
            n %= 1000000
        if n >= 100000:
            parts.append(convert_tens(n // 100000, units, tens) + "แสน")
            n %= 100000
        if n >= 10000:
            parts.append(convert_tens(n // 10000, units, tens) + "หมื่น")
            n %= 10000
        if n >= 1000:
            parts.append(convert_tens(n // 1000, units, tens) + "พัน")
            n %= 1000
        if n >= 100:
            parts.append(convert_tens(n // 100, units, tens) + "ร้อย")
            n %= 100
        if n > 0:
            parts.append(convert_tens(n, units, tens))
            
        return "".join(parts)
    
    def convert_decimal_part(n):
        if n > 0 and n <= 99:
            ten_part = n // 10
            unit_part = n % 10
            if unit_part == 0:
                return tens[ten_part] + "สตางค์"
            elif unit_part == 1 and ten_part > 0:
                return tens[ten_part] + "เอ็ด" + "สตางค์"
            else:
                return tens[ten_part] + units[unit_part] + "สตางค์"
        return ""
    
    integer_part = int(num)
    decimal_part = round((num - integer_part) * 100)

    result = convert_integer_part(integer_part) + "บาท"
    if decimal_part > 0:
        result += convert_decimal_part(decimal_part)
    else:
        result += "ถ้วน"
    return result


def format_number(event):
    user_input = entry.get().replace(",", "").strip()
    if user_input.isdigit() or (user_input.replace(".", "").isdigit() and user_input.count(".") == 1):
        integer_part, *decimal_part = user_input.split(".")
        formatted_number = "{:,}".format(int(integer_part))
        if decimal_part:
            formatted_number += "." + decimal_part[0]
        entry.delete(0, tk.END)
        entry.insert(0, formatted_number)

def convert():
    try:
        user_input = entry.get().replace(",", "").strip()
        if not user_input:
            raise ValueError("กรุณากรอกจำนวนเงิน")
        
        if user_input.count(".") > 1:
            raise ValueError("กรุณาป้อนค่าที่มีจุดทศนิยมได้เพียง 1 จุดเท่านั้น (ห้ามมีจุดทศนิยมซ้ำกัน)")
        
        # ตรวจสอบรูปแบบทศนิยม
        if "." in user_input:
            integer_part, decimal_part = user_input.split(".")
            if len(decimal_part) > 2:
                raise ValueError("โปรแกรมรับค่าทศนิยมได้สูงสุด 2 ตำแหน่งเท่านั้น (0-99 สตางค์)")
        
        # ตรวจสอบว่าผู้ใช้ป้อนค่าที่เป็นตัวเลขหรือไม่
        if not re.match(r"^\d+(\.\d{1,2})?$", user_input):
            raise ValueError("กรุณาป้อนค่าเป็นตัวเลขหรือจำนวนเงินเท่านั้น")
        
        # แปลงตัวเลข
        number = float(user_input)
        if number > 9999999999999.99:
            raise ValueError("โปรแกรมรองรับการแปลงจำนวนเงินสูงสุด 9,999,999,999,999.99 บาท")
        
        result = number_to_thai(number)
        result_label.config(text=f"ผลลัพธ์: {result}")
    except ValueError as e:
        messagebox.showerror("ข้อผิดพลาด", str(e))


# ส่วนของ GUI
root = tk.Tk()
root.title("แปลงตัวเลขเป็นคำภาษาไทย")

# ส่วนรับข้อมูล
tk.Label(root, text="กรอกจำนวนเงิน:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=1, padx=10, pady=10)
entry.bind("<KeyRelease>", format_number)  # จับเหตุการณ์เมื่อผู้ใช้พิมพ์

# ปุ่มแปลง
convert_button = tk.Button(root, text="แปลง", command=convert)
convert_button.grid(row=0, column=2, padx=10, pady=10)

# ส่วนแสดงผล
result_label = tk.Label(root, text="ผลลัพธ์: ", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# เริ่มต้นโปรแกรม
root.mainloop()
