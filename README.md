# Easy Video/Audio Cutter Extractor

This Python script allows you to easily extract specific sequences from video or audio files by specifying the start and end times in seconds. The script supports a variety of file formats and is easy to use from the command line.

## Features

- Extract sequences from video files (e.g., MP4, AVI, MOV, MKV).
- Extract sequences from audio files (e.g., MP3, WAV, AAC, FLAC).
- Specify start and end times in seconds.
- Supports a wide range of input formats.
- Output files retain the original format.

## Requirements

- Python 3.6+
- `moviepy` library
- `opencv-python` (optional, only if you are using video manipulation)
- `numpy` library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AyoubJAdouli/easy_video_cutter_extractor.git
   cd easy_video_cutter_extractor
   python cut.py <file_path> <start_time> <end_time> <output_path>
 
   ```
