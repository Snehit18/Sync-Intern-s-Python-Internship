# Import necessary libraries
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from time import sleep
import pygame.mixer
from threading import Thread
from PIL import ImageTk, Image

# Create a main window
window = Tk()
window.title('Alarm Clock')
window.geometry('590x300')
window.configure(bg='white smoke')

# Create a top frame for a line separator
frame_line = Frame(window, width=590, height=10)
frame_line.grid(row=0, column=0)
frame_line.configure(bg='seashell4')

# Create a main frame for the body
frame_body = Frame(window, width=590, height=290)
frame_body.grid(row=1, column=0)
frame_body.configure(bg='LightSkyBlue3')

# Load an image and resize it
img = Image.open('alarm_clock.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

# Create an image label
app_image = Label(frame_body, height=150, image=img)
app_image.place(x=30, y=60)
app_image.configure(bg='LightSkyBlue3')

# Create label for the application name
name = Label(frame_body, text='Alarm Clock', height=2, font=('Ivy 20 bold'), bg='LightSkyBlue3')
name.place(x=190, y=20)

# Create label and combobox for selecting hour
hour = Label(frame_body, text='Hour', height=2, font=('Ivy 16 bold'), bg='LightSkyBlue3')
hour.place(x=190, y=75)
c_hour = Combobox(frame_body, width=2, font=('Ivy 16'))
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)
c_hour.place(x=193, y=120)

# Create label and combobox for selecting minutes
minutes = Label(frame_body, text='Minutes', height=2, font=('Ivy 16 bold'), bg='LightSkyBlue3')
minutes.place(x=260, y=75)
c_minutes = Combobox(frame_body, width=4, font=('Ivy 16'))
c_minutes['values'] = tuple(f"{i:02}" for i in range(60))
c_minutes.current(0)
c_minutes.place(x=263, y=120)

# Create label and combobox for selecting seconds
seconds = Label(frame_body, text='Seconds', height=2, font=('Ivy 16 bold'), bg='LightSkyBlue3')
seconds.place(x=360, y=75)
c_seconds = Combobox(frame_body, width=5, font=('Ivy 16'))
c_seconds['values'] = tuple(f"{i:02}" for i in range(60))
c_seconds.current(0)
c_seconds.place(x=363, y=120)

# Create label and combobox for selecting period
period = Label(frame_body, text='Period', height=2, font=('Ivy 16 bold'), bg='LightSkyBlue3')
period.place(x=470, y=75)
c_period = Combobox(frame_body, width=3, font=('Ivy 16'))
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=473, y=120)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print("Deactivated alarm: ", selected.get())
    pygame.mixer.music.stop()

# Create a variable to store the selected value
selected = IntVar()

# Create a radio button for saving
rad1 = Radiobutton(frame_body, height=2, font=('Ivy 16 bold'), value=1, bg='LightSkyBlue3', text='Activate', command=activate_alarm, variable=selected)
rad1.place(x=193, y=180)

def alarm_sound():
    pygame.mixer.music.load('alarm_sound.mp3')
    pygame.mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frame_body, height=2, font=('Ivy 16 bold'), value=2, bg='LightSkyBlue3', text='Deactivate', command=deactivate_alarm, variable=selected)
    rad2.place(x=320, y=180)

def alarm():
    while selected.get() == 1:
        alarm_hour = c_hour.get()
        alarm_minutes = c_minutes.get()
        alarm_seconds = c_seconds.get()
        alarm_period = c_period.get()
        alarm_period = alarm_period.upper()
        now = datetime.now()

        hour = now.strftime("%I")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        period = now.strftime("%p")

        if alarm_period == period:
            if alarm_hour == hour:
                if alarm_minutes == minutes:
                    if alarm_seconds == seconds:
                        print("Time to take a break!!")
                        alarm_sound()
                        break  # Exit the loop once the alarm goes off
        sleep(1)

# Initialize the mixer
pygame.mixer.init()

# Start the main event loop
window.mainloop()
