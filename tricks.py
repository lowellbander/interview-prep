""" Transforming Code into Beautiful, Idiomatic Python by Raymond Hettinger
http://pyvideo.org/video/1780/transforming-code-into-beautiful-idiomatic-pytho
"""

from itertools import izip

def main():
    """a main routine using some of the neat examples from the video"""

    names = ['raymond', 'rachel', 'matthew']
    colors = ['red', 'green', 'blue', 'yellow']

    for color in reversed(colors):
        print color

    for name, color in izip(names, colors):
        print name, '-->', color
