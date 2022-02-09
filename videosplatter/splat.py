import argparse
import math
import os
import re
import subprocess

import PIL.Image
import cv2
import imageio_ffmpeg
import numpy as np
from moviepy.editor import VideoFileClip

FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


def get_metadata(filename):
    result = subprocess.run([FFMPEG_BINARY, '-i', filename], capture_output=True)
    video_info = result.stderr.decode()
    fps = re.search(r'(\d\d(\.\d\d)?) fps', video_info).group(1)
    
    runtime_string = re.search(r'Duration: (\d\d:\d\d:\d\d.\d\d)', video_info).group(1)
    hours, mins, secs = runtime_string.split(':')

    return int(hours) * 3600 + int(mins) * 60 + float(secs), fps


def get_color(image):
    data = np.reshape(image, (-1, 3))
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    compactness, labels, centers = cv2.kmeans(data, 1, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    return centers[0].reshape((-1, 3))


def barcode(filename, start, end, interval):
    clip = VideoFileClip(filename)
    end = end or int(clip.duration)
    colors = [get_color(clip.get_frame(timestamp)) for timestamp in range(start, end, interval)]
    height = int(len(colors) * .2)
    bar_image = np.transpose(np.tile(np.array(colors, dtype=np.uint8), (height, 1)), axes=(1, 0, 2))
    return PIL.Image.fromarray(bar_image)


def splat(filename, start, end, interval):
    total_duration, fps = get_metadata(filename)
    
    splat_duration = (end or float(total_duration)) - start
    
    image_count = math.ceil(splat_duration / interval)
    row_count = math.ceil(image_count / 12)
    
    sample_frequency = math.ceil(float(fps) * interval)
    
    col_count = 6 if image_count < 180 else 12
    filter_string = f'select=not(mod(n\,{sample_frequency})),scale=360:-1,tile={col_count}x{row_count}'
    
    output_filename = os.path.splitext(filename)[0] + '_splat.jpg'
    subprocess.run([FFMPEG_BINARY, '-ss', str(start), '-i', filename, '-frames', '1', '-vf', filter_string, output_filename])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='video file to splatter')
    parser.add_argument('--start', type=int, default=0, help='start time in seconds')
    parser.add_argument('--end', type=int, default=None, help='end time in seconds')
    parser.add_argument('-i', '--interval', type=int, default=10, help='how many seconds between images')
    parser.add_argument('-b', '--barcode', action='store_true', help='barcode mode. create a "barcode" of all the colors in the video')

    args = parser.parse_args()

    if args.barcode:
        image = barcode(args.file, args.start, args.end, args.interval)
        image.save(os.path.splitext(args.file)[0] + '_barcode.jpg')
    else:
        splat(args.file, args.start, args.end, args.interval)


if __name__ == '__main__':
    main()

