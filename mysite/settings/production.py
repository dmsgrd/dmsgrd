# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
with open('secret_key_production.txt') as f:
    SECRET_KEY = f.read().strip()