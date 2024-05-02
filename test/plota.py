# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:37:37 2020

@author: 86152
"""
import matplotlib.pyplot as plt
import numpy as np

a=np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')
plt.show()