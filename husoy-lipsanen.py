from collections import Counter

import argparse
import os
import os.path
import matplotlib.pyplot as plt
import numpy as np

FILETYPES = 'gif jpeg jpg ppt png doc xls xlsx svg txt csv pdf tex'.split()

def main():
    args = get_arguments()
    frequencies = get_frequencies(args.personal_directory)
    histogram(frequencies)


def get_arguments():
    argparser = argparse.ArgumentParser('husoy-lipsanen')
    argparser.add_argument('personal_directory', help='The directory to run the profiling on')
    return argparser.parse_args()


def get_frequencies(directory):
    counter = Counter()
    for root, dirs, files in os.walk(directory):
        print('Couting files in %s...' % root)
        counter.update(os.path.splitext(file)[1][1:] for file in files)
    return counter


def histogram(frequencies):
    elements = [frequencies[t] for t in FILETYPES]
    y_pos = np.arange(len(elements))
    plt.barh(y_pos, elements, align='center')
    plt.yticks(y_pos, FILETYPES)
    plt.show()

if __name__ == '__main__':
    main()
