from tkinter import *
from pytube import YouTube


def download(link):
    youtubeobject = YouTube(link)
    youtubeobject = youtubeobject.streams.get_highest_resolution()
    try:
        youtubeobject.download()
    except:
        print("There has been an error in downloading the video")
    print("the video has downloaded!!")
    

def dw():
    link = input_km.get()
    download(link)


window = Tk()
window.title("YT Downloader")
window.minsize(width=250, height=125)
window.config(padx=20, pady=20)

url_label = Label(text="URL:")
url_label.grid(column=0, row=0)
url_label.config(padx=10, pady=10)

input_km = Entry()
input_km.grid(column=1, row=0)
input_km.config(width=15)

calc_button = Button(text="Download", command=dw, font=("Arial", 12, "bold"))
calc_button.grid(column=1, row=2)
calc_button.config(padx=5, pady=5)

window.mainloop()
