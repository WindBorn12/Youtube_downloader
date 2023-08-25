import pytube

url = str(input("enter url  "))
path = ""
pytube.YouTube(url).streams.get_highest_resolution().download(path)