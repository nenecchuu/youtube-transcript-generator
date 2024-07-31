import re

class TranscriptFormatter:
    def clean_vtt_lines(self, vtt_lines):
        result = vtt_lines[:3]
        result.append('\n')
        seen = []
        current_caption = []
        current_start_time = None
        current_end_time = None

        def merge_and_append_caption():
            nonlocal current_caption, current_start_time, current_end_time
            if current_caption:
                for caption_text in current_caption:
                    if caption_text not in seen:
                        result.append(f"{current_start_time} --> {current_end_time}\n")
                        result.append(caption_text + '\n\n')
                        seen.append(caption_text)
                    current_caption = []

        for i in range(4, len(vtt_lines)):
            line = vtt_lines[i]
            if '-->' in line:
                if current_start_time is not None:
                    merge_and_append_caption()
                current_start_time, current_end_time = line.strip().split(' --> ')
                current_end_time = current_end_time.split(' ')[0]
            elif line.strip() == '':
                continue
            else:
                line = re.sub(r'<c>|</c>|<\d{2}:\d{2}:\d{2}\.\d{3}>|\[.*?\]', '', line).strip()
                if line:
                    if current_caption and current_caption[-1].endswith(line):
                        current_caption[-1] += ' ' + line
                    else:
                        current_caption.append(line)

        if current_start_time is not None:
            merge_and_append_caption()

        final_result = []
        previous_line_was_empty = False
        for line in result:
            if line.strip() == '':
                if not previous_line_was_empty:
                    final_result.append(line)
                previous_line_was_empty = True
            else:
                final_result.append(line)
                previous_line_was_empty = False
        
        transcript = ' '.join(seen)
        return {'final_result': final_result, 'transcript': transcript}
