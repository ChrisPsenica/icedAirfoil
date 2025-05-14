# plot data for pressure profile on the airfoil model (both baseline and rime model)
# 05/12/2025

#---------- imports ----------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#---------- Read In Data ----------
# read in csv files with pressure data
dataBaseline = pd.read_csv('pBaseline.csv' , delimiter = ',')  
dataRime = pd.read_csv('pRime.csv' , delimiter = ',')  

# extract last column from csv files (the pressure data)
pBaseline = dataBaseline.iloc[:, -1] ; chordBaseline = dataBaseline.iloc[:, 0]  
pRime = dataRime.iloc[:, -1] ; chordRime = dataRime.iloc[:, 0]

#---------- Plot Data ----------
# plot baseline
plt.figure()
plt.plot(chordBaseline , pBaseline)
plt.title('Pressure Profile for Baseline Airfoil' , color = 'b')
plt.xlabel('Airfoil Surface')
plt.ylabel('Pressure (Pa)')
plt.grid()
plt.show(block = False)

# plot rime
plt.figure()
plt.plot(chordRime , pRime)
plt.title('Pressure Profile for Rime Iced Airfoil' , color = 'b')
plt.xlabel('Airfoil Surface')
plt.ylabel('Pressure (Pa)')
plt.grid()
plt.show()
