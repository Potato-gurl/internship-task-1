import tkinter as tk
from tkinter import ttk

def convert_temp():
    temp=float (entry_temp.get())
    from_unit=combo_from.get()
    to_unit=combo_to.get()

    if from_unit=="celsius":
        if to_unit=="fahrenheit":
             result=(temp*9/5)+32
        elif to_unit=="kelvin":
            result=temp+273.15
        else:
            result=temp   

    elif from_unit=="fahrenheit":
        if to_unit=="celsius":
            result=(temp-32)*5/9
        elif to_unit=="kelvin":    
            result=(temp-32)*5/9+273.15
        else:
            result=temp

    elif from_unit=="kelvin":
        if to_unit=="celsius":
            result=temp-273.15
        elif to_unit=="fahrenheit":
            result=(temp-273.15)*9/5+32
        else:
            result=temp

    label_result.config(text=f"result: {round(result,2)}{to_unit}")   


app=tk.Tk()
app.title("temprature convertor")
app.geometry("350x350")
app.configure(bg="#F98DDE")

title=tk.Label(app,text="temprature convertor",font=("Arial",16,"bold"),bg="#f5f5f5")
title.pack(pady=10)


entry_temp=tk.Entry(app,font=("Arial",12),justify="center")
entry_temp.pack(pady=10)
entry_temp.insert(0,"enter temprature")


units=["celsius","fahrenheit","kelvin"]


combo_from=ttk.Combobox(app,values=units,state="readonly")
combo_from.set("celsius")
combo_from.pack(pady=5)

combo_to=ttk.Combobox(app,values=units,state="readonly")
combo_to.set("fahrenheit")
combo_to.pack(pady=5)


btn=tk.Button(app,text="convert",font=("Arial",12),bg="#ce46ac",fg="white",command=convert_temp)
btn.pack(pady=15)


label_result=tk.Label(app,text="result:",font=("Arial",12),bg="#ffffff")
label_result.pack(pady=10)

app.mainloop()


