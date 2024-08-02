from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root=Tk()
root.title("Weather App")
root.geometry("250x100")
root.iconbitmap("weather-2019-02-07.png")

def ziplookup():
    '''
    zip.get()
    zipLabel=Label(root,text=zip.get())
    zipLabel.grid(row=1,column=0,columnspan=2)
    '''
    new=Tk()
    new.title("Air Quality Lookup:")
    new.geometry("350x75")
    #to connect to a third party API out in the www and bring data back we import requets:
    try:
        api_request=requests.get("https://api.waqi.info/search/?token=d10fab6e38558d284ceb280ebfc38f671d77ac62&keyword="+city.get())
        api=json.loads(api_request.content)
        aqi=api["data"][0]['aqi']
        lab1=Label(new,text=aqi)
        lab1.grid(row=0,column=0)
        
        if 0<=aqi<=50:
            weather_color="#0C0"
            #quality="Good air quality"
            myLabel=Label(new,text="Good air qualit")
            myLabel.grid(row=1,column=0)

        elif  50<aqi<=100:
            weather_color="#FFFF00"
            #quality="Moderate air quality"
            myLabel=Label(new,text="Moderate air quality")
            myLabel.grid(row=1,column=0)

        elif 100<aqi<=200:
            weather_color="#ff9900"
            #quality="Unhealthy air quality"
            myLabel=Label(new,text="Unhealthy air quality")
            myLabel.grid(row=1,column=0)
            

        elif 300<aqi<=500:
            weather_color="#FF0000"
            #quality="Very Unhealthy air quality"
            myLabel=Label(new,text="Very Unhealthy air quality")
            myLabel.grid(row=1,column=0)

        elif aqi>500:
            weather_color="#990066"
            #quality="Hazardous air quality"
            myLabel=Label(new,text="Hazardous air quality")
            myLabel.grid(row=1,column=0)

        new.configure(background=weather_color)
        myLabel=Label(text=" ",background=weather_color)
        myLabel.grid(row=1,column=0)

        
    
    except Exception as e:
        api="Error..."
        

btn1=Label(root,text="City: ")
btn1.grid(row=0,column=0)
btn2=Label(root,text=" ")
btn2.grid(row=1,column=0)
city=Entry(root)
city.grid(row=0,column=1)

zipbtn=Button(root,text="Search",command=ziplookup)
zipbtn.grid(row=2,column=1)

root.mainloop()