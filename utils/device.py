# decompyle3 version 3.9.2
# Python bytecode version base 3.9.0 (3425)
# Decompiled from: Python 3.9.18 (main, Sep 11 2023, 13:41:44) 
# [GCC 11.2.0]
# Embedded file name: /home/samir.ait-abbou/Bureau/assistant-logement/utils/device.py
# Compiled at: 2025-06-25 14:57:36
# Size of source mod 2**32: 111 bytes


# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.9


import torch

def detect_device():
    if torch.cuda.is_available():
        return 'cuda'
    return 'cpu'