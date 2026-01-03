import customtkinter as ctk
import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        result_entry.configure(state='normal')
        result_entry.delete(0, 'end')
        result_entry.insert(0, "Ошибка: введите число!")
        result_entry.configure(state='readonly')
        return
    chars = string.ascii_letters + string.digits
    if spec_var.get() == 1:
        chars += string.punctuation
    
    password = "".join(random.choice(chars) for _ in range(length))
    
    result_entry.configure(state='normal')
    result_entry.delete(0, 'end')
    result_entry.insert(0, password)
    result_entry.configure(state='readonly')

root = ctk.CTk()
root._set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.geometry("450x300")
root.title("Password Pro")

label_title = ctk.CTkLabel(root, text="Генератор паролей", font=("Arial", 20, "bold"))
label_title.pack(pady=20)

entry_length = ctk.CTkEntry(root, placeholder_text="Введите длину (напр. 12)", width=250)
entry_length.pack(pady=10)

spec_var = ctk.IntVar(value=0)
checkbox_spec = ctk.CTkCheckBox(root, text="Использовать спецсимволы (!@#$)", variable=spec_var)
checkbox_spec.pack(pady=10)

btn_generate = ctk.CTkButton(root, text="Создать пароль", command=generate_password)
btn_generate.pack(pady=20)

result_entry = ctk.CTkEntry(root, width=300, justify="center", fg_color="transparent", state="readonly")
result_entry.pack(pady=10)

root.mainloop()