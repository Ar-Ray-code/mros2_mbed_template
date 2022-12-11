#!/usr/bin/env python3
import argparse
import os
import subprocess

def clean(args):
    if args.clean:
        this_dir = os.path.dirname(os.path.abspath(__file__))
        rm_r_command = 'rm -rf ' + this_dir + '/.ccache/* ' + this_dir + '/cmake_build'
        subprocess.call(rm_r_command, shell=True)
        print('Cleaned')
        exit(0)
    else :
        return

def build(args):
    target = args.target
    if target == 'UNKNOWN':
        import inquirer
        target_list = [
            'NUCLEO_F767ZI',
            'NUCLEO_F746ZG',
            'DISCO_F746NG'
        ]

        # question for target
        questions = [
            inquirer.List('target',
                            message="Select target",
                            choices=target_list,
                        ),
        ]

        # answer
        answers = inquirer.prompt(questions)
        target = answers['target']

    # command
    command = 'docker run --rm -t -u $(id -u):$(id -g) \
        --mount=type=bind,source="$(pwd)",destination=/var/mbed \
        --mount=type=bind,source="$(pwd)/.ccache",destination=//.ccache \
        -w /var/mbed ghcr.io/armmbed/mbed-os-env \
        bash -c "mbed-tools deploy \
        && mbed-tools compile -t GCC_ARM -m ' + target + '"'

    print(command)
    # execute command
    subprocess.call(command, shell=True)


args = argparse.ArgumentParser()
args.add_argument('--target', type=str, default='UNKNOWN')
args.add_argument('--clean', action='store_true')
args = args.parse_args()

clean(args)
build(args)