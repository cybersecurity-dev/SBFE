#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pathlib import Path

from pyfiglet import Figlet
def print_banner():
    f_b = Figlet(font='big')
    print(f_b.renderText('SFET'))
    f_s = Figlet(font='slant')
    print(f_s.renderText('Static Feature Extraction Tool for Potentially Malicious OS Files'))

import yaml
def read_system_conf(param_cfg : Path = Path('conf/sfet.yml')):
    try:
        with open(param_cfg, 'r') as file:
            config = yaml.safe_load(file)

        mlw_dir = config.get('malware_dataset_dir')
        bng_dir = config.get('benign_dataset_dir')

    except FileNotFoundError:
        print("Error: conf.yml file not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except KeyError as e:
        print(f"Error: {e} not found in {param_cfg}")
    return mlw_dir, bng_dir

def main():
    print_banner()
    mlw_dir, bng_dir = read_system_conf()

if __name__ == "__main__":
    main()