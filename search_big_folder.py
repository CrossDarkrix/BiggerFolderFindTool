#!python3
# coding: utf-8

import concurrent.futures
import os
import sys

class findBigFolder(object):
    def __init__(self, path: str='{}{}'.format(os.curdir, os.sep)):
        concurrent.futures.ThreadPoolExecutor().submit(self.search, path)

    def get_size_dir(self, path: str='{}{}'.format(os.curdir, os.sep)):
        total_size = 0
        for dir_path in os.listdir(path):
            full_path = os.path.join(path, dir_path)
            if os.path.isfile(full_path):
                total_size += os.path.getsize(full_path)
            elif os.path.isdir(full_path):
                total_size += self.get_size_dir(full_path)
        return total_size

    def search_folders(self, path: str='{}{}'.format(os.curdir, os.sep)):
        for root, dirs, files, in os.walk(path):
            for directory in dirs:
                yield os.path.join(root, directory)

    def search(self, path: str='{}{}'.format(os.curdir, os.sep)):
        folder_json = {}
        founded_dir = ['']
        for dirs in self.search_folders(path):
            try:
                if not founded_dir[0] in dirs.split(os.sep)[-2:]:
                    if 10.00 <= round(self.get_size_dir(dirs) / 1024 / 1024, 2):
                        folder_json[dirs] = '{}MB'.format(round(self.get_size_dir(dirs) / 1024 / 1024, 2))
                        founded_dir[0] = dirs.split(os.sep)[-1]
            except:
                pass
        print('\n'.join(sorted(list(set(['{}: {}'.format(key, value) for key, value in folder_json.items()])), reverse=True)))

def main():
    if len(sys.argv) != 2:
        print('{} [path]'.format(sys.argv[0].split(os.sep)[-1]))
    elif sys.argv[1] == '--help':
        print('{} [path]'.format(sys.argv[0].split(os.sep)[-1]))
    elif sys.argv[1] == '-h':
        print('{} [path]'.format(sys.argv[0].split(os.sep)[-1]))
    else:
        findBigFolder(sys.argv[1])

if __name__ == '__main__':
    main()