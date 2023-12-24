from pytube import YouTube

def download_video(video_url, output_path='vids'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        video_title = yt.title

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Set the output path (default is the current working directory)
        video_stream.download(output_path)

        return (f"Video downloaded successfully to {output_path}"), video_title
    except Exception as e:
        return (f"An error occurred: {e}"), None

# Example usage:
# video_url = "https://www.youtube.com/watch?v=SBzNGLKBpbo"
# output_path = "vids"

# download_video(video_url, output_path)
