from pathlib import Path
from typing import List
import yt_dlp
import io
import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

import haikunator

gen = haikunator.Haikunator()

def download_video(base_path: str, url: str):
    file_name = gen.haikunate()
    file_path = f'{base_path}/{file_name}.mp4'
    ydl_opts = {
        'outtmpl': file_path,
        'merge_output_format': 'mp4',
        'format': 'bestvideo+bestaudio/best',
    }
    try:
    # Create a YoutubeDL instance with the options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Start the download
            ydl.download(urls)
    except yt_dlp.utils.DownloadError as e:
        print(f"An error occurred during download: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return file_path

def edit_as_movie(path: str, comment: str):
    font_path = "/Library/Fonts/SF-Pro-Display-Medium.otf" 
    font_size = 48
    clip = VideoFileClip(path)


    txt_clip = TextClip(
            font=font_path,
            text=comment,
            color='black',
            font_size=font_size,
            text_align="center",
            method="label",
            duration=clip.duration,

    )
    video = CompositeVideoClip([clip, txt_clip])  
    video.write_videofile(path.replace('.mp4', '_edited.mp4'), codec='libx264', audio_codec='aac')
    clip.close()




# Define the TikTok URL (or any other supported URL)
urls = ['https://www.tiktok.com/t/ZP8jQsjo8/']# Replace with an actual URL



path = download_video('./files', urls[0])
edit_as_movie(path, "Jarrett hates jews and eats butt cheeks")