import yt_dlp

def get_available_formats(url):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        mp4_formats = [f for f in formats if f['ext'] == 'mp4' or f['ext'] == 'm4a']
        for f in mp4_formats:
            if f['format'].endswith(')'):
                print(f"Format ID: {f['format_id']}, Format: {f['format']}, Resolution: {f['resolution']}, Extension: {f['ext']}")
        return mp4_formats

def download_youtube_video(url, format_choice):
    ydl_opts = {
        'format': format_choice,
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': '%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage

url = input("Enter URL: ")
formats = get_available_formats(url)
format_choice = input("\n\nEnter the format ID you want to download: ")
for f in formats:
    if f['format_id'] == format_choice:
        download_youtube_video(url, format_choice)
        break
