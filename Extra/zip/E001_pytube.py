from pytube import YouTube

try:
    yt = YouTube('https://youtu.be/A8KQhwmdZIw')
    print(yt.title)
    print(yt.thumbnail_url)
    yt_stream = yt.streams.get_highest_resolution()
    yt_stream.download(".\\")
except Exception as e:
    print(e)
