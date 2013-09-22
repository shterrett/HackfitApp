import data_in_direct
import smooth_curve
import find_peaks
import get_weight

# data is expected in the form of [time, x-accel, y-accel, z-accel] into 
# data-in. data_in returns a list of z-accel only.

data = data_in_direct.start_collection()
accel_data = get_accel_data(data)
weight_data = get_weight_data(data)
smooth_data = smooth_curve.smoothListGaussian(accel_data)
peaks = find_peaks.find_peaks(smooth_data)
weight = get_weight.get_weight(weight_dat)
print peaks
print weight

def get_accel_data(data):
  return [x[0] for x in data]

def get_weight_data(data):
  return [x[1] for x in data]
