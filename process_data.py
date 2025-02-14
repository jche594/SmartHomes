import numpy as np
import datetime as datetime
import pandas as pd
from solver import model_home  
from helper import get_half_hour_index, get_all_indices_for_time_ranges

data = pd.read_csv('data.csv')

#  Define prices
tariff = data.iloc[0, 1:4].to_numpy()
offpeak_indices = get_all_indices_for_time_ranges(["9:00 PM - 7:00 AM"])
shoulder_indices = get_all_indices_for_time_ranges(["9:00 AM - 5:00 PM"])
peak_indices = get_all_indices_for_time_ranges(["7:00 AM - 9:00 AM", "5:00 PM - 9:00 PM"])

p = np.zeros(48)
p[offpeak_indices] = tariff[2] 
p[shoulder_indices] = tariff[1] 
p[peak_indices] = tariff[0] 

# Define demand
d = data.iloc[0, 4:52].to_numpy()

# Define excess price as $99/kWh
e = np.full(48, 99)

# Define Hours of Free Power
hop_indices = get_all_indices_for_time_ranges(["9:30 PM - 10:30 PM"])    
p[hop_indices] = 0

# if __name__ == "__main__":
x = model_home(p, d, e)

print(np.dot(x,p))