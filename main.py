import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets():
    head_label = Label(root, text="YouTube Video Downloader", padx=15, pady=15, font="SegoeUI 14", bg="white", fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    link_label = Label(root, text="YouTube link:", bg="red", pady=7, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)
    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Destination:", bg="red", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)
    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Browse", command=Browse, width=10, bg="yellow", relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    Download_B = Button(root, text="Download Video", command=Download, width=20, bg="blue", pady=10, padx=15, relief=GROOVE, font="Georgia, 13")
    Download_B.grid(row=4, column=1, pady=20, padx=20)

    # Bind Ctrl+V (paste) to the linkText Entry widget
    root.linkText.bind("<Control-v>", paste_from_clipboard)

def paste_from_clipboard(event):
    clipboard_text = root.clipboard_get()
    root.linkText.delete(0, END)
    root.linkText.insert(0, clipboard_text)

def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)

def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(output_path=download_Folder)

    root.clipboard_clear()
    root.clipboard_append(Youtube_link)
    root.update()

    messagebox.showinfo("Download Success", "Video Downloaded Successfully")
root = tk.Tk()
root.title("YouTube Video Downloader")
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()