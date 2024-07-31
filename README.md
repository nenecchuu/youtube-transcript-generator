# YouTube Transcript Downloader and Formatter

## Project Description

This project provides a utility to download YouTube video transcripts (subtitles) and format them for better readability. The tool using `yt-dlp` to fetch subtitles and then processes the subtitle files to produce cleaned and well-formatted outputs. The formatted transcripts are saved in a specified output directory with customizable file names.

## Features

- Download automatic subtitles from YouTube videos.
- Clean and format subtitle files for better readability.
- Save formatted subtitle files and transcripts with custom names.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- `yt-dlp` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/yt-transcript-formatter.git
    cd yt-transcript-formatter
    ```

2. Install the required dependencies:

    ```sh
    pip install yt-dlp
    ```

## Usage

1. Run the main script to download and format YouTube subtitles:

    ```sh
    python main.py
    ```

2. Enter the YouTube video URL when prompted.

3. The script will download the subtitles, format them, and save the output files in the `output` directory with the names:
    - `<filename>.vtt`
    - `<filename>.txt`