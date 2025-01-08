import tkinter
import customtkinter
import yt_dlp

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

label = customtkinter.CTkLabel(app, text="Enter YouTube URL:")
label.pack(pady=20)

url_entry = customtkinter.CTkEntry(app, width=500, placeholder_text="Paste YouTube link here...")
url_entry.pack(pady=10)

status_label = customtkinter.CTkLabel(app, text="", text_color="white")
status_label.pack(pady=10)

def download_video():
    url = url_entry.get()
    if url.strip():
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  
                'merge_output_format': 'mp4',         
                'postprocessors': [{           
                    'key': 'FFmpegVideoConvertor',  
                    'preferedformat': 'mp4',        
                }],
                'outtmpl': '%(title)s.%(ext)s',       
                'n_threads': 4,                       
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status_label.configure(text="Download completed!", text_color="green")
        except Exception as e:
            status_label.configure(text=f"Error: {e}", text_color="red")
            print(f"Error: {e}")
    else:
        status_label.configure(text="Please enter a valid YouTube URL.", text_color="red")

download_button = customtkinter.CTkButton(app, text="Download", command=download_video)
download_button.pack(pady=20)

app.mainloop()

