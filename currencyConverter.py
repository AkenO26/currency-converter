import tkinter as tk
import tkinter.ttk as ttk
import requests

main_window = tk.Tk()
main_window.title("Currency converter")
w = 350; h = 200
main_window.minsize(w, h); main_window.maxsize(w, h)
ws = main_window.winfo_screenwidth()
hs = main_window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))


api_key = "api key "
base_url = "http://api.exchangeratesapi.io/v1/latest"


r= ""
def button_pressed():
    amount2 = amount.get()
    source = source_c.get()
    target = target_c.get()
    url = base_url + "?access_key=" + str(api_key) + "&base="+ source
    request = requests.get(url)
    reponse = request.json()
    r =reponse["rates"][target]*float(amount2)  #bad practice but that's all i can do with this API whithout paying
    conversion_label.config(text = str(round(r, 2))+" "+ target)


label_greeting = tk.Label(main_window, text ="Welcome to Live Currency Convertor", relief = 'raised', fg = "white", bg = "blue", borderwidth = 3, font = "Courier 15 bold")
main_window.grid_columnconfigure(0, weight =1)
label_greeting.grid(row =0)

amount = tk.StringVar()
textfield = tk.Entry(main_window, justify = "right", textvariable = amount)
textfield.grid(row = 1, padx = 5, pady = 5)


source_c = tk.StringVar()
currency = ["USD", "EUR", "HUF", "GBP", "CHF", "JPY"]
start_currencyBox = ttk.Combobox(main_window, values = currency, textvariable = source_c)
start_currencyBox.grid(row = 2)

target_c = tk.StringVar()
target_currencyBox = ttk.Combobox(main_window, values = currency,textvariable = target_c)
target_currencyBox.grid(row = 3)

convertButton = tk.Button(main_window, text = "Convert", height = 1, width = 7, command = button_pressed)
convertButton.grid(row = 4)

conversion_label = tk.Label(main_window, text ="")
conversion_label.grid(row = 5)






main_window.mainloop()