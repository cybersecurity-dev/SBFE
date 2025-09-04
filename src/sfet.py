#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pyfiglet import Figlet

if __name__ == '__main__':

    f_b = Figlet(font='big')
    print(f_b.renderText('SFET'))
    f_s = Figlet(font='slant')
    print(f_s.renderText('Static Feature Extraction Tool for Potentially Malicious OS Files'))