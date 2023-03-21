"""ITHome automatic check in.
Based on https://github.com/daimiaopeng/ithome_qiandao
"""

import argparse
import os
from concurrent.futures import process

from run import run

if __name__ == '__main__':
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    run(username, password)
