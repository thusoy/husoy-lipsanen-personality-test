from collections import Counter

import argparse
import os
import os.path
import matplotlib.pyplot as plt
import numpy as np

_DEFAULT_FILETYPES = 'gif,jpeg,jpg,ppt,png,doc,xls,xlsx,svg,txt,csv,pdf,tex'

def main():
    args = get_arguments()
    frequencies = get_frequencies(args.personal_directory, args.ignore)
    histogram(frequencies, args.types)


def get_arguments():
    argparser = argparse.ArgumentParser('husoy-lipsanen')
    argparser.add_argument('personal_directory', help='The directory to run the profiling on')
    argparser.add_argument('-t', '--types', default=_DEFAULT_FILETYPES,
        help='Comma-separated list of extensions to use for the graphing. Default: %(default)s')
    argparser.add_argument('-i', '--ignore', help='Directory names to ignore. Default: %(default)s')
    args = argparser.parse_args()
    args.types = args.types.split(',')
    args.ignore = set(args.ignore.split(','))
    return args


def get_frequencies(directory, ignore_dirs):
    counter = Counter()
    for root, dirs, files in os.walk(directory):
        dir_set = set(dirs) - ignore_dirs
        dirs[:] = list(dir_set)
        print('Analyzing files in %s...' % root)
        counter.update(os.path.splitext(file)[1][1:] for file in files)
    return counter


def histogram(frequencies, filetypes):
    elements = [frequencies[t] for t in filetypes]
    y_pos = np.arange(len(elements))
    plt.barh(y_pos, elements, align='center')
    plt.yticks(y_pos, filetypes)
    plt.show()

if __name__ == '__main__':
    main()
