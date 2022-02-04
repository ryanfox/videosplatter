import argparse
import math
import os
import re
import subprocess

import imageio_ffmpeg


FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


def get_metadata(filename):
    result = subprocess.run([FFMPEG_BINARY, '-i', filename], capture_output=True)
    video_info = result.stderr.decode()
    fps = re.search('(\d\d(\.\d\d)?) fps', video_info).group(1)
    
    runtime_string = re.search('Duration: (\d\d:\d\d:\d\d.\d\d)', video_info).group(1)
    hours, mins, secs = runtime_string.split(':')

    return int(hours) * 3600 + int(mins) * 60 + float(secs), fps


def splat(filename, start, end, interval):
    total_duration, fps = get_metadata(filename)
    
    splat_duration = (end or float(total_duration)) - start
    
    image_count = math.ceil(splat_duration / interval)
    row_count = math.ceil(image_count / 12)
    
    sample_frequency = math.ceil(float(fps) * interval)
    
    col_count = 6 if image_count < 180 else 12
    filter_string = f'select=not(mod(n\,{sample_frequency})),scale=360:-1,tile={col_count}x{row_count}'
    
    output_filename = os.path.splitext(filename)[0] + '.jpg'
    subprocess.run([FFMPEG_BINARY, '-ss', str(start), '-i', filename, '-frames', '1', '-vf', filter_string, output_filename])
