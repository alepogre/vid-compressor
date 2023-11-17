import os
import subprocess


def compress_video(input_path, output_folder, resolution):
    try:
        # Create the Output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Set the output file name based on the input file name
        output_file = os.path.join(output_folder, os.path.basename(input_path))

        # Use FFmpeg to compress the video
        subprocess.run(['ffmpeg', '-i', input_path, '-vf', f'scale={resolution}',
                        '-c:a', 'aac', '-strict', 'experimental', output_file])
        print(f"Compression successful. Output file: {output_file}")

    except Exception as e:
        print(f"Error during compression: {e}")


if __name__ == "__main__":
    # Set the input folder path
    input_folder_path = 'Input'

    # Choose the desired resolution (720p or 1080p)
    chosen_resolution = '1280x720'  # Change this to '1280x720' for 720p or '1920x1080' for 1080p

    # Set the output folder path
    output_folder_path = 'Output'

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder_path):
        if filename.endswith(('.mp4', '.avi', '.mkv', '.mov')):  # Add more video file extensions if needed
            input_file_path = os.path.join(input_folder_path, filename)
            compress_video(input_file_path, output_folder_path, chosen_resolution)
