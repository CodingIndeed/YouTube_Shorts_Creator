from gtts import gTTS
import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, TextClip, ColorClip, CompositeVideoClip
import time
from mutagen.mp3 import MP3
import requests
import json
import random
import textwrap
import subprocess
import pyautogui



def download_video(query, orientation):
   # Define the endpoint URL
   url = "https://api.pexels.com/videos/search"

   # Define the query parameters
   params = {
      "query": query,
      "orientation": orientation,
      "size": "medium",
      "color": "",
      "locale": "",
      "min_duration": "25",
      "page": "1",
      "per_page": "20"
   }

   # Define the headers (replace 'YOUR_API_KEY' with your actual API key)
   headers = {
      "Authorization": "YOUR_API_KEY" #for pexels
   }

   # Send the GET request
   response = requests.get(url, params=params, headers=headers)

   # Convert the response to JSON
   json_response = response.json()

   # Convert the generator to a list
   search_videos = list(json_response['videos'])

   # Generate a random index
   random_index = random.randint(0, len(search_videos) - 1)

   # Get the video at the random index
   video = search_videos[random_index]

   # Construct the download URL
   data_url = 'https://www.pexels.com/video/' + str(video['id']) + '/download'

   # Send GET request to the download URL
   r = requests.get(data_url)

   # Write the content of the response to a file
   with open('video.mp4', 'wb') as outfile:
      outfile.write(r.content)
      print("Background video download complete!")

      # Resize the video to the desired resolution
   subprocess.call(['ffmpeg', '-i', 'video.mp4', '-vf', 'scale=-1:1080', 'Background_video.mp4'])

def quoteFunction():
    category = 'success'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'}) #for api-ninjas
    if response.status_code == requests.codes.ok:
        data = response.text
        parsed_data = json.loads(data)
        quote = parsed_data[0]['quote']
        return quote
    else:
        print("Error:", response.status_code, response.text)

def text_to_mp3(text, output_file):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')

    # Save the generated speech as an MP3 file
    tts.save(output_file)
    print(f"Text converted to {output_file}")

def add_text_and_audio_to_video(video, audio, background_music, Text):
    screen_width, screen_height = pyautogui.size()
    base_font_size = 45
    scaling_factor = screen_width / 1920  # Assuming 1920x1080 as base resolution
    font_size = int(base_font_size * scaling_factor)

    try:
        clip = VideoFileClip(video)
        audio_clip = AudioFileClip(audio)
        background_music_clip = AudioFileClip(background_music)
    except Exception as e:
        print(f"Could not open video file {video}: {str(e)} or {audio}: {str(e)}")
        return

    Audio_Duration = MP3("Quote.mp3").info.length
    video_duration = clip.duration

    # If the Audio_Duration is greater than the video duration, loop the video
    if Audio_Duration > video_duration:
        # Calculate the number of times the video needs to be looped
        loops = int(Audio_Duration // video_duration)

        # Create a temporary file for the looped video
        temp_video = "temp_video.mp4"

        # Use FFmpeg command to loop the video
        os.system(f"ffmpeg -stream_loop {loops} -i {video} -c copy {temp_video}")

        # Replace the original video with the looped video
        clip = VideoFileClip(temp_video)

    # Create a black color clip with opacity of 0.5
    color_clip = ColorClip((clip.size[0], clip.size[1]), col=[0, 0, 0]).set_opacity(0.75)

    # Wrap the text
    wrapper = textwrap.TextWrapper(width=20)
    lines = wrapper.wrap(Text)

    # Join the lines back together with \n
    Text = '\n'.join(lines)

    txt_clip = TextClip(Text, fontsize=font_size, color='white', font="Candara-Bold")
    txt_clip = txt_clip.set_position('center').set_duration(Audio_Duration)

    video = CompositeVideoClip([clip, color_clip, txt_clip])
    # Set the audio of the video
    final_audio = CompositeAudioClip([audio_clip, background_music_clip])
    video = video.set_audio(final_audio)
    video = video.set_duration(Audio_Duration)
    video.write_videofile("Final_video.mp4", audio_codec='aac')
    clip.close()
    print("Added text and audio to video!")

def delete_file(file_path1, file_path2, file_path3, file_path4):
    if os.path.isfile(file_path1):
        os.remove(file_path1)
        print(f"{file_path1} deleted successfully.")
    else:
        print(f"{file_path1} does not exist.")

    if os.path.isfile(file_path2):
        os.remove(file_path2)
        print(f"{file_path2} deleted successfully.")
    else:
        print(f"{file_path2} does not exist.")

    if os.path.isfile(file_path3):
        os.remove(file_path3)
        print(f"{file_path3} deleted successfully.")
    else:
        print(f"{file_path3} does not exist.")

    if os.path.isfile(file_path4):
        os.remove(file_path4)
        print(f"{file_path4} deleted successfully.")
    else:
        print(f"{file_path4} does not exist.")




if __name__ == "__main__":


    Text = quoteFunction()

    backgroundMusic = "Background_audio.mp3" #Path to the background song for the video
    outputAudio = "Quote.mp3"

    download_video("success", "portrait")

    time.sleep(1)

    text_to_mp3(Text, outputAudio)

    video_path = "Background_video.mp4" 

    time.sleep(5)

    add_text_and_audio_to_video(video_path, outputAudio, backgroundMusic, Text)
    #add_text_to_video(video_path, Text, outputAudio)


    #add_audio_to_video(outputAudio, backgroundMusic)

    time.sleep(5)

    delete_file("Quote.mp3", "Background_video.mp4", "temp_video.mp4", "video.mp4")

