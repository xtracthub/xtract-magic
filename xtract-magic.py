import os
import sys
import magic
from itertools import chain
from pprint import pp


def flatten(nested_list):
    return list(chain.from_iterable(nested_list))


xtract_magic = magic.Magic(
    mime=True,
    mime_encoding=True,
    keep_going=True,
    raw=True,
    extension=True
)


def get_paths(dir_path):
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path)
                  if os.path.isfile(os.path.join(dir_path, f))]


def run_file(file_path=None):
    if not file_path:
        return
    mdata = xtract_magic.from_file(file_path)
    mdata = mdata.split(";")
    for idx,m in enumerate(mdata):
        mdata[idx] = m.split("\n-")
        mdata[idx] = [n.strip() for n in mdata[idx]]
    return flatten(mdata)


def run_dir(dir_path):
    if not dir_path:
        dir_path = str(os.getcwd())
    file_paths = get_paths(dir_path)
    bundled_metadata = dict()
    for file_path in file_paths:
        bundled_metadata[file_path] = run_file(file_path)
    return bundled_metadata


if __name__ == "__main__":
    dir = sys.argv[1]
    mdata = run_dir(dir)
    pp(mdata)
