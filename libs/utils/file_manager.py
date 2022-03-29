import glob
import os
import logging


class FileManager:
    @classmethod
    def clean_directory(cls, dir_path, ignore_pattern=None):
        files = glob.glob(f'{dir_path}/*')
        for file_ in files:
            if ignore_pattern:
                if ignore_pattern not in file_:
                    cls.remove_file(file_)
            else:
                cls.remove_file(file_)

    @staticmethod
    def remove_file(file_path):
        os.remove(file_path)
        logging.log(logging.DEBUG, f'Removed file by path {file_path}.')
