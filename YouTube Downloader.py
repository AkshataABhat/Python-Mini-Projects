from pytube import YouTube
link=input("Enter URL: ")
yt=YouTube(link)
videos=yt.streams.all()
video=list(enumerate(videos))
for i in video:
    print(i)

dn_option=int(input("Enter the format you want to download the video: "))
dn_video=videos[dn_option]
dn_video.download()
print("Downloaded Successfully")
