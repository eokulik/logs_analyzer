import os


def get_files(dirname: str) -> list:
    if os.path.isfile(dirname):
        with open(dirname, 'r') as log_file:
            yield log_file.readlines()
    elif os.path.isdir(dirname):
        for filename in os.listdir(dirname):
            with open('{0}/{1}'.format(dirname, filename), 'r') as log_file:
                yield log_file.readlines()
