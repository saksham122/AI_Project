import tkinter as tk
import requests

def weatherap(can):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=288dd86d0aaf3758140660d52e9625dc"
    
    json_data = requests.get(api).json()
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15 )
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    final_result = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temperature: " + str(max_temp) + "\n" + "Min Temperature: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "Kmpr"
    label1.config(text = final_result)
    label2.config(text = final_data)

can = tk.Tk()
can.geometry("600x500")
can.title("Noise Weather App")

f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(can, justify='center', width = 20, font = t)
textfield.pack(pady=20)
textfield.focus
textfield.bind('<Return>', weatherap)

label1 = tk.Label(can, font=t)
label1.pack()
label2 = tk.Label(can, font=f)
label2.pack()
can.mainloop()

