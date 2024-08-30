import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import AudioFileClip

def extract_sequence(file_path, start_time, end_time, output_path):
    # Determine if the file is video or audio
    if file_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        # Process as video file
        with VideoFileClip(file_path) as video:
            # Cut the video
            video_sequence = video.subclip(start_time, end_time)
            # Write the result
            video_sequence.write_videofile(output_path, codec='libx264')
    elif file_path.lower().endswith(('.mp3', '.wav', '.aac', '.flac')):
        # Process as audio file
        with AudioFileClip(file_path) as audio:
            # Cut the audio
            audio_sequence = audio.subclip(start_time, end_time)
            # Write the result
            audio_sequence.write_audiofile(output_path)
    else:
        raise ValueError("Unsupported file type. Please provide a valid audio or video file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract a sequence from an audio or video file.",
        epilog="Example usage: python extract_sequence.py input.mp4 30 60 output.mp4"
    )

    parser.add_argument(
        "file_path", 
        type=str, 
        help="Path to the input audio or video file. Supported formats include mp4, avi, mov, mkv for video; mp3, wav, aac, flac for audio."
    )
    parser.add_argument(
        "start_time", 
        type=float, 
        help="Start time of the sequence in seconds. For example, use 30 to start from 30 seconds."
    )
    parser.add_argument(
        "end_time", 
        type=float, 
        help="End time of the sequence in seconds. For example, use 60 to end at 60 seconds."
    )
    parser.add_argument(
        "output_path", 
        type=str, 
        help="Path to save the extracted sequence. The extension should match the type of the input file (e.g., mp4 for video, mp3 for audio)."
    )

    args = parser.parse_args()

    extract_sequence(args.file_path, args.start_time, args.end_time, args.output_path)
