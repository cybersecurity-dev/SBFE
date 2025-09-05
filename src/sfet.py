#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pyfiglet import Figlet
def print_banner():
    f_b = Figlet(font='big')
    print(f_b.renderText('SFET'))
    f_s = Figlet(font='slant')
    print(f_s.renderText('Static Feature Extraction Tool for Potentially Malicious OS Files'))

def main():
    print_banner()

if __name__ == "__main__":
    main()