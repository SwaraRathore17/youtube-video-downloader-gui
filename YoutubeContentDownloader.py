import yt_dlp
import time
from tkinter import *
from tkinter import messagebox  # For pop-up notifications
import os

import os

class YtDownload:
    def __init__(self, geometry):
        location = os.path.join(os.environ["USERPROFILE"], "Videos", "Youtube downloads")
        if not os.path.exists(location):
            os.makedirs(location)


        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Download Youtube Video")
        self.root.resizable(False, False)
        self.root.geometry(geometry)
        self.VideoLink = Entry(self.root, border=4, font=("Times", 15))
        Label(self.root, text='Youtube Videos', fg='red', bg='black', font=('Times', 25)).place(x=150, y=30)
        Label(self.root, text='(Enter The url)', fg='red', bg='black', font=('Times', 25)).place(x=160, y=70)
        self.VideoLink.place(x=25, y=120, height=40, width=450)

        def GetVideo(resolution, format):
            ydl_opts = {
    'paths': {'default': location},
    'outtmpl': '%(resolution)s_%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
    'noplaylist': True,
}

            try:
                link = self.VideoLink.get()
                ydl_opts = {
                    'outtmpl': location + '%(resolution)s_%(title)s.%(ext)s',
                    'noplaylist': True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(link, download=False)
                    formats = info_dict.get('formats', [])

                    available_resolutions = [
                        str(f.get('height')) for f in formats if f.get('height') is not None
                    ]

                    StartTime = time.time()
                    self.root.destroy()

                    if format == 'mp4':
                        if str(resolution) not in available_resolutions:
                            messagebox.showinfo("Quality Not Found", 
                                f"The requested quality ({resolution}p) is not available.\nDownloading best available quality instead.")
                            ydl_opts['format'] = 'bestvideo+bestaudio/best'
                        else:
                            ydl_opts['format'] = f'bestvideo[height={resolution}]+bestaudio/best'

                    elif format == 'mp3':
                        ydl_opts['format'] = 'bestaudio'

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link])

                    EndTime = time.time()
                    print(f"Download Completed in {int(EndTime - StartTime)} seconds.")

            except Exception as a:
                print(a.__class__.__name__)
                if a.__class__.__name__ == "FileExistsError":
                    print("File Already Exists")
                elif a.__class__.__name__ == "RegexMatchError":
                    print("Please enter a valid URL of the video")
                elif a.__class__.__name__ == "AttributeError":
                    print("Unable to download file. Check if the selected option is available.")
                else:
                    print("An unexpected error occurred:", a)

        # Download quality buttons
        Button(self.root, text="144p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(144, 'mp4')).place(x=50, y=200)
        Button(self.root, text="240p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(240, 'mp4')).place(x=150, y=200)
        Button(self.root, text="360p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(360, 'mp4')).place(x=250, y=200)
        Button(self.root, text="480p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(480, 'mp4')).place(x=350, y=200)
        Button(self.root, text="720p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(720, 'mp4')).place(x=50, y=280)
        Button(self.root, text="1080p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(1080, 'mp4')).place(x=150, y=280)
        Button(self.root, text="1440p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(1440, 'mp4')).place(x=250, y=280)
        Button(self.root, text="2160p", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(2160, 'mp4')).place(x=350, y=280)
        Button(self.root, text="Audio", font=('Times', 20, 'bold'), fg='red', border=3, command=lambda: GetVideo(360, 'mp3')).place(x=200, y=360)

        self.root.mainloop()

# Launch the app
a = YtDownload("500x500")