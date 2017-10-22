# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:18:20 2017

@author: Administrator
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("gui/循环 往返.xlsx")
plt.plot(data.time, data.a,'b', data.time, data.b,'g')



