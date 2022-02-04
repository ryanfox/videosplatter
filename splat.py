import argparse

from videosplatter import splat


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='video file to splatter')
    parser.add_argument('--start', type=int, default=0, help='start time in seconds')
    parser.add_argument('--end', type=int, default=None, help='end time in seconds')
    parser.add_argument('-i', '--interval', type=int, default=10, help='how many seconds between images')
    args = parser.parse_args()
    
    splat.splat(args.file, args.start, args.end, args.interval)


if __name__ == '__main__':
    main()
