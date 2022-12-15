from pytube import YouTube


def download(link):
    youtubeobject = YouTube(link)
    youtubeobject = youtubeobject.streams.get_highest_resolution()
    try:
        youtubeobject.download()
    except:
        print("There has been an error in downloading the video")
    print("the video has downloaded!!")

link = input("Put your youtube link here URL: ")

download(link)
