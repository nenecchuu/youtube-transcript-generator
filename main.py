import os
import re
from transcript import YoutubeTranscriptDownloader
from formatter import TranscriptFormatter
from constants import TEMP_DOWNLOADED_OUTPUT_FILENAME, SUBTITLE_FORMAT, OUTPUT_DIR

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def main():
    video_url = input("Enter the YouTube video URL: ")
    downloader = YoutubeTranscriptDownloader()
    formatter = TranscriptFormatter()
    
    lang = downloader.get_original_caption_lang(video_url)
    if not lang:
        print("No subtitles found for this video.")
        return

    video = downloader.download_subtitle(video_url, lang)
    downloaded_file_name = f"{TEMP_DOWNLOADED_OUTPUT_FILENAME}.{lang}.{SUBTITLE_FORMAT}"

    with open(downloaded_file_name, 'r', encoding='utf-8') as file:
        vtt_content = file.readlines()

    formatted_result = formatter.clean_vtt_lines(vtt_content)

    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Determine the output filenames
    base_filename = sanitize_filename(video['title'])
    output_vtt_file = os.path.join(OUTPUT_DIR, f'{base_filename}.vtt')
    transcript_file = os.path.join(OUTPUT_DIR, f'{base_filename}.txt')

    # Save the formatted VTT file
    with open(output_vtt_file, 'w', encoding='utf-8') as file:
        file.writelines(formatted_result['final_result'])

    # Save the transcript file
    with open(transcript_file, 'w', encoding='utf-8') as file:
        file.write(formatted_result['transcript'])

    print(f"Formatted VTT saved to {output_vtt_file}")
    print(f"Transcript saved to {transcript_file}")

    # Remove temp file
    os.remove(downloaded_file_name)

if __name__ == "__main__":
    main()
