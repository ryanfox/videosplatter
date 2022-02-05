from videosplatter import splat

from gooey import Gooey, GooeyParser


@Gooey(program_name='Videosplatter')
def main():
    parser = GooeyParser(description='Splat a video into frames and show them all at once')
    parser.add_argument('file', help='Video file to splatter', widget='FileChooser')
    parser.add_argument('--start', type=int, default=0, help='Start time in seconds')
    parser.add_argument('--end', type=int, default=None, help='End time in seconds')
    parser.add_argument('-i', '--interval', type=int, default=10, help='How many seconds between images')
    args = parser.parse_args()

    splat.splat(args.file, args.start, args.end, args.interval)


if __name__ == '__main__':
    main()

