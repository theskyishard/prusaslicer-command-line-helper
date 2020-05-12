import sys
import subprocess
import argparse

def parseArguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "-target", dest='target', type=str, required=True)
    parser.add_argument("-p", "-profile", dest='profile', type=str, required=True)

    parser.add_argument("--u", dest='userParameters', type=str, default="")

    args = parser.parse_args()
    return args    

def main(target, profile, userParameters):
    command = "prusa-slicer-console.exe --export-gcode {} --output \"output\" --load \"{}\" {}".format(target, profile, userParameters)
    print(command)
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    args = parseArguments()
    main(args.target, args.profile, args.userParameters)