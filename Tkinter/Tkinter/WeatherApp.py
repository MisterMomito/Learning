from tkinter import *
from PIL import ImageTk, Image
import requests
import json

# how do i make it so that the label showing the info is erased before new info is placed?

root = Tk()
root.geometry('400x100')


def zip_lookup():
    global my_label
    # zip.get()
    # zip_label = Label(root, text=zip.get())
    # zip_label.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() +
            '&distance=25&API_KEY=40E3D313-B6D4-4AB2-827C-DDDD1454A79A')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = '#00e400'
        elif category == 'Moderate':
            weather_color = '#ffff00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff7e00'
        elif category == 'Unhealthy':
            weather_color = '#ff0000'
        elif category == 'Very Unhealthy':
            weather_color = '#8f3f97'
        elif category == 'Hazardous':
            weather_color = '#7e0023'

        root.configure(background=weather_color)

        my_label = Label(root, text=city + ' Air Quality ' + str(quality) + ' ' + category, font=('Helvetica', 20),
                         background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = 'Error...'


zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zip_button = Button(root, text='Lookup Zipcode', command=zip_lookup)
zip_button.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()
