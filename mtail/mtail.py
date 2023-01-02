#!/usr/bin/env python3

import argparse
import os
import shutil
from collections import deque
from glob import glob
from time import sleep


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", default=None, type=int, help="Number of lines to tail")
    parser.add_argument("-t", default=5, type=float, help="Seconds between checks")
    parser.add_argument("files", nargs="+", help="Log files")
    args = parser.parse_args()

    try:
        while True:
            files = []
            for file_glob in args.files:
                files.extend(glob(file_glob))
            files.sort()

            for _ in range(10):
                print()

            os.system('cls' if os.name == 'nt' else 'clear')

            if files:
                terminal_size = shutil.get_terminal_size((120, 50))
                length = terminal_size.columns
                height = args.n or (terminal_size.lines - 1) // len(files) - 1
                assert height >= 1
                assert length >= 10

                for file in files:
                    print("\u001b[7m" + file + " " * (length - len(file)) + "\u001b[0m")
                    try:
                        lines = deque(maxlen=height)
                        for _ in range(height):
                            lines.append("")
                        for line in open(file):
                            has_cr = "\r" in line
                            line = line.replace("\r", "")
                            line = line.strip()
                            if not line:
                                continue
                            if has_cr or ("] - " in line and "] - " in lines[-1]) or (
                                    "it/s" in line and "it/s" in lines[-1]) or ("s/it" in line and "s/it" in lines[-1]):
                                lines[-1] = line
                            else:
                                lines.append(line)
                        for line in lines:
                            print(line[:length])
                    except Exception as e:
                        print(e)
            else:
                print("\u001b[7m No files to tail. \u001b[0m")

            sleep(args.t)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
