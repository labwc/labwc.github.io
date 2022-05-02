#!/usr/bin/env python3
#
# Really ought to try to understand+fix this upstream, but for now, let's just
# get it working
#

import sys

def main(argv):
    with open(argv[0], 'r') as file:
        buf = file.read()

    buf = buf.replace("·</p>\n<p>", "· ")

    with open(argv[0], 'w') as file:
        file.write(buf)

if __name__ == "__main__":
    main(sys.argv[1:])

