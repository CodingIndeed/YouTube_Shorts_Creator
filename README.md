# YouTube Shorts Video Creator

This Python script automates the creation of YouTube Shorts videos by downloading background videos, overlaying inspirational quotes, and adding both speech synthesis and background music. Utilizing APIs from Pexels for video and API Ninjas for quotes, this script simplifies the process of generating engaging and motivational content suitable for the YouTube Shorts platform.

## Prerequisites

Before running this script, ensure you have the following:

- Python 3.x installed on your system.
- A valid API key from [Pexels](https://www.pexels.com/api/) for video downloads.
- A valid API key from [API Ninjas](https://api-ninjas.com/) for fetching quotes.
- FFMPEG installed on your system for video processing.

## Installation

To use this script, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python libraries as shown below:
   - `gtts` for Google Text-to-Speech.
   - `moviepy` for video editing.
   - `mutagen` for audio file metadata handling.
   - `requests` for making API requests.
   - `pyautogui` for determining screen size (optional, used for font scaling).

## Usage

To create a YouTube Shorts video, follow these steps:

1. Replace `'YOUR_API_KEY'` placeholders in the script with your actual Pexels and Ninjas API keys.
2. Customize the `Text` variable or modify the `quoteFunction` to change the category of quotes fetched.
3. Change the `backgroundMusic` variable to the path of your desired background audio file.
4. Run the script with `python youtube_shorts_creator.py`.

**Note:** The script downloads a random video based on the search query and orientation provided, overlays a quote fetched from API Ninjas, converts the quote into speech, and combines everything with optional background music to produce a final video titled "Final_video.mp4".

## Contributions

Contributions to this project are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request. Your contributions can help make this project even better.

