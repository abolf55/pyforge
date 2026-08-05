import tkinter as tk

mainform = tk.Tk()
mainform.geometry("340x360")
mainform.resizable(width=False, height=False)
mainform.title("ماشین حساب")
mainform.configure(bg="#d9d9d9")

# -------------------- منطق و توابع محاسباتی --------------------

def press_key(char):
    current = entry1.get()
    if current == "Error":
        entry1.delete(0, tk.END)
    entry1.insert(tk.END, char)

def clear():
    entry1.delete(0, tk.END)

def backspace():
    current = entry1.get()
    if current == "Error":
        entry1.delete(0, tk.END)
    else:
        entry1.delete(len(current) - 1, tk.END)

def calculate():
    try:
        expression = entry1.get()
        # جایگزینی علامت‌های بصری برای ارزیابی ریاضی
        expression = expression.replace("x", "*")
        
        # پیشگیری صریح از تقسیم بر صفر برای جلوگیری از خطای ZeroDivisionError
        if "/0" in expression or "%0" in expression:
            entry1.delete(0, tk.END)
            entry1.insert(0, "Error")
            return
            
        result = eval(expression)
        
        # تبدیل عدد اعشاری به صحیح در صورت بدون اعشار بودن مقدار (.0)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        entry1.delete(0, tk.END)
        entry1.insert(0, str(result))
    except Exception:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Error")

def toggle_sign():
    current = entry1.get()
    if current == "Error":
        entry1.delete(0, tk.END)
        return
    if not current:
        return
    try:
        if current.startswith("-"):
            entry1.delete(0, 1)
        else:
            entry1.insert(0, "-")
    except Exception:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Error")

# -------------------- اتصالات کیبورد --------------------

def key_event(event):
    char = event.char
    if char in "0123456789.+-*/%":
        press_key(char)
    elif char == "\r" or char == "=":
        calculate()
    elif char == "\b":
        backspace()
    elif event.keysym == "Escape":
        clear()

mainform.bind("<Key>", key_event)

# -------------------- فیلد ورودی --------------------

entry1 = tk.Entry(mainform, fg="black", bg="white", font=("Arial", 18), justify="right")
entry1.place(x=10, y=10, width=320, height=50)

# -------------------- دکمه‌های اعداد --------------------

btn_1 = tk.Button(mainform, text="7", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("7"))
btn_1.place(x=10, y=120, width=75, height=45)

btn_2 = tk.Button(mainform, text="8", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("8"))
btn_2.place(x=90, y=120, width=75, height=45)

btn_3 = tk.Button(mainform, text="9", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("9"))
btn_3.place(x=170, y=120, width=75, height=45)

btn_4 = tk.Button(mainform, text="4", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("4"))
btn_4.place(x=10, y=170, width=75, height=45)

btn_5 = tk.Button(mainform, text="5", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("5"))
btn_5.place(x=90, y=170, width=75, height=45)

btn_6 = tk.Button(mainform, text="6", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("6"))
btn_6.place(x=170, y=170, width=75, height=45)

btn_7 = tk.Button(mainform, text="1", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("1"))
btn_7.place(x=10, y=220, width=75, height=45)

btn_8 = tk.Button(mainform, text="2", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("2"))
btn_8.place(x=90, y=220, width=75, height=45)

btn_9 = tk.Button(mainform, text="3", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("3"))
btn_9.place(x=170, y=220, width=75, height=45)

btn_10 = tk.Button(mainform, text="0", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("0"))
btn_10.place(x=90, y=270, width=75, height=45)

# -------------------- دکمه‌های علائم ریاضی --------------------

btn_11 = tk.Button(mainform, text="C", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=clear)
btn_11.place(x=10, y=70, width=75, height=45)

btn_12 = tk.Button(mainform, text="<-", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=backspace)
btn_12.place(x=90, y=70, width=75, height=45)

btn_13 = tk.Button(mainform, text="%", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("%"))
btn_13.place(x=170, y=70, width=75, height=45)

btn_14 = tk.Button(mainform, text="/", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("/"))
btn_14.place(x=255, y=70, width=75, height=45)

btn_15 = tk.Button(mainform, text="*", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("*"))
btn_15.place(x=255, y=120, width=75, height=45)

btn_16 = tk.Button(mainform, text="-", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("-"))
btn_16.place(x=255, y=170, width=75, height=45)

btn_17 = tk.Button(mainform, text="+", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("+"))
btn_17.place(x=255, y=220, width=75, height=45)

btn_18 = tk.Button(mainform, text="+/-", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=toggle_sign)
btn_18.place(x=10, y=270, width=75, height=45)

btn_19 = tk.Button(mainform, text=".", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=lambda: press_key("."))
btn_19.place(x=170, y=270, width=75, height=45)

btn_20 = tk.Button(mainform, text="=", bg="#a8d8ea", fg="black", font=("Arial", 16, "bold"), command=calculate)
btn_20.place(x=255, y=270, width=75, height=45)

mainform.mainloop()
