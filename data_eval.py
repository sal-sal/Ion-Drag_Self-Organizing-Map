# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:58:37 2024

@author: Sali
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

load_filename = 'VM2_AVI_231005_114720_100pa_1mA_neg'
folder_csv = 'csv_files'

#%%

pressure = np.array([120, 120, 100, 100, 90, 90, 70, 70, 60, 60])
error    = np.array([6.9919, 3.9419, 8.3686, 5.1514, 8.5119, 6.5791, 11.3347, 10.5353, 15.0162, 10.8872])
mean_v   = np.array([0.007617, 0.003777, 0.016163, 0.008016, 0.040292, 0.037159, 0.031784, 0.050557, 0.260084, 0.116349])

plt.figure(dpi=500)
plt.plot(pressure, mean_v, 'x')
plt.plot(pressure, mean_v, '--')
plt.xlabel('pressure [Pa]')
plt.ylabel('mean velocity [mm/s]')
plt.show()




