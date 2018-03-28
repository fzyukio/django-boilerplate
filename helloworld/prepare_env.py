import os
import random
import string

import yaml

from shutil import copyfile

__all__ = ['config']

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

filename = os.path.join(base_dir, 'settings.yaml')
default_filename = os.path.join(base_dir, 'settings.default.yaml')

# If file "settings.yaml" doesn't exist, create one from template
if not os.path.isfile(filename):
    copyfile(default_filename, filename)
    with open(filename, 'a', encoding='utf-8') as f:

        # And generate a random key
        secret = ''.join([random.SystemRandom().choice(
            "{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)])
        f.write('secret_key: {}'.format(secret))

with open(filename, 'r', encoding='utf-8') as f:
    config = yaml.load(f)

config['base_dir'] = base_dir



