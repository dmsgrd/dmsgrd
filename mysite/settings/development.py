# -*- coding: utf-8 -*-
import os
from .base import *

DEBUG = True

with open(os.path.join(BASE_DIR, "mysite/settings/secret_key.txt")) as f:
    SECRET_KEY = f.read().strip()

