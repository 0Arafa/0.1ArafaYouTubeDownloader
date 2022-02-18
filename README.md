# 0.1ArafaYouTubeDownloader
YouTube Video and MP3 Downloader, tested on Windows and Linux.

==========================

We need a pafy library to download a videos from YouTube.
We need an os library to check if the file is already installed and execute the youtube-dl command and clear The Terminal.
We need a time library to sleep one second when we finish.
We need a termcolor library to make our Tool more beautiful.
We need a platform library to know what is the operating system we're using and execute the right command for clear The Terminal.

==========================

Windows:
    If you don't have any of these libraries, open your CMD and write: pip3 install [The_Library]
    If you don't have a youtube-dl in your CMD, you can go to Google and type: How to install youtube-dl in Windows CMD.
    ----------------------------------
    Common Issues:
       1: If you have this problem: ffprobe/avprobe and ffmpeg/avconv not found. Please install one.
          Open Google and write: Fix problem ffprobe/avprobe and ffmpeg/avconv not found. Please install one in youtube-dl.
       2: If you have TypeError: dislike_count
          Go to this file: dist-packages/pafy/backend_youtube_dl.py, and edit it
          And go to this line : self._dislikes = self._ydl_info['dislike_count']
          And comment it, it will be like this: #self._dislikes = self._ydl_info['dislike_count']
----------------------------------

Linux:
    If you don't have any of these libraries, open your Terminal and write: pip3 install [The_Library]
    If you don't have youtube-dl, open your Terminal and write: sudo apt install youtube-dl
    ----------------------------------
    Common Issue:
        If you have TypeError: dislike_count
        Go to your Terminal and type this:  nano /usr/local/lib/python3.9/dist-packages/pafy/backend_youtube_dl.py
        And go to this line : self._dislikes = self._ydl_info['dislike_count']
        And comment it, it will be like this: #self._dislikes = self._ydl_info['dislike_count']

-----------------------------------
