#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:05:17 2020

@author: amary
@Email: taufik.amary@gmail.com
"""

import numpy as np
import pandas as pd

data_wine_red = pd.read_csv('winequality-red.csv')
print(data_wine_red.head())
data_wine_red.groupby('quality').size()