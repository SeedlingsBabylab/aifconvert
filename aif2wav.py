import sys
import os
import subprocess as sp

def crawl(start_dir):
    for root, dirs, files in os.walk(start_dir):
            for file in files:
                if file.endswith(".aif"):
                    convert_file(os.path.join(root, file))

def convert_file(file):
    new_file = file.replace(".aif", ".wav")

    command = ["ffmpeg",
                   "-i",
                   file,
                   new_file]

    command_string = " ".join(command)
    print command_string

    pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)
    out, err = pipe.communicate()

if __name__ == "__main__":
    start_dir = sys.argv[1]

    crawl(start_dir)
