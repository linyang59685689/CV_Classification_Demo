# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/5 下午8:44
# @Author: LiLinYang
# @File  : yang_test.py

import torch
import sys
import os
print(torch.cuda.is_available())
path='../Dataset/train/chickens/chickens046.jpg'
print(os.path.isfile(path))