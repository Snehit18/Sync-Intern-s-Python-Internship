import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("URL Shortner")
root.geometry("500x200")
root.configure(bg='seashell4')

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)

longurl_label = tkinter.Label(root, text="Enter Long URL", font=('Helvetica', 10, 'bold'), bg='seashell4')
longurl_entry = tkinter.Entry(root, width=40)
shorturl_label = tkinter.Label(root, text="Shortened URL", font=('Helvetica', 10, 'bold'), bg='seashell4')
shorturl_entry = tkinter.Entry(root, width=40)
shorten_button = tkinter.Button(root, text="Shorten URL", font=('Helvetica', 10, 'bold'), bg='steel blue', command=shorten)

longurl_label.pack(pady=10)
longurl_entry.pack()
shorturl_label.pack(pady=10)
shorturl_entry.pack()
shorten_button.pack(pady=15)

root.mainloop()