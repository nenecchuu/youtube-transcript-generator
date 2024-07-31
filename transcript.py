import yt_dlp
from constants import TEMP_DOWNLOADED_OUTPUT_FILENAME, SUBTITLE_FORMAT

class YoutubeTranscriptDownloader:
    def __init__(self):
        self.ydl_opts = {'listsubtitles': True}

    def get_original_caption_lang(self, video_url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            result = ydl.extract_info(video_url, download=False)
        automatic_captions = result.get('automatic_captions', {})
        for lang, _ in automatic_captions.items():
            if '-orig' in lang:
                return lang
        return None

    def download_subtitle(self, video_url, lang):
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': [lang],
            'subtitlesformat': SUBTITLE_FORMAT,
            'skip_download': True,
            'outtmpl': TEMP_DOWNLOADED_OUTPUT_FILENAME + '.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            subtitles = info_dict.get('automatic_captions', {}).get(lang)
            if not subtitles:
                print(f"No automatic captions found for the '{lang}' language.")
                return
            ydl.download([video_url])
            print(f"Downloaded automatic captions for '{video_url}' in '{lang}' language.")
            
        return info_dict
