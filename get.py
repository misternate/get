# usr/bin/env python
import argparse
from genericpath import exists
import re
import os

import requests
from tqdm import tqdm


def download_file(path, chunk_size=1024):
    if args.directory:
        os.makedirs(args.directory, exist_ok=True)
        directory = args.directory + "/"
    else:
        directory = ""

    if args.name:
        filename = args.name
    else:
        filename = get_filename(path)

    r = requests.get(path, allow_redirects=True, stream=True)
    total = int(r.headers.get("content-length", 0))
    with open(directory + filename, "wb") as file, tqdm(
        desc=filename,
        total=total,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in r.iter_content(chunk_size=chunk_size):
            file.write(data)
            bar.update(chunk_size)


def get_filename(path):
    return re.findall("(?:.+\/)([^#?]+)", args.path)[0]


parser = argparse.ArgumentParser(
    description="Get is a small little downloader utility."
)
parser.add_argument("path", type=str, help="Downloads the path entered.")
parser.add_argument("--name", "-n", help="Use a custom name for the downloaded file.")
parser.add_argument(
    "--directory", "-d", help="Create or add the downloaded file to a directory."
)
args = parser.parse_args()

if args.path:
    download_file(args.path)
