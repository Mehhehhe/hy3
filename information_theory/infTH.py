import numpy as np

freq_array = [
    0.1275,0.0925,0.085,
    0.0775,0.0775,0.075,
    0.0725,0.06,0.0425,
    0.0375,0.035,0.035,
    0.03,0.03,0.0275,
    0.0275,0.0225,0.02,
    0.015,0.015,0.0125,
    0.005,0.005,0.005,0.0025
]

hx = freq_array * np.log2(freq_array)
sum = 0
for i in hx:
    sum = sum + i

print(sum)
