# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:57:49 2020

@author: 86152
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='SimHei'
plt.plot([3,1,4,5,2])
plt.ylabel("纵轴（值）")
plt.savefig('test',dpi=600)
plt.show()