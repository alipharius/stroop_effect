import random
import psychopy
import time
import csv
from pathlib import Path


class Trial:
    def __init__(self, id, word, ink_color)