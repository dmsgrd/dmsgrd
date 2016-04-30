# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

with open('secret_key.txt') as f:
    SECRET_KEY = f.read().strip()