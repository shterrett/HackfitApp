import matplotlib.pyplot as plt
import data_in_direct
import smooth_curve
import find_peaks
import get_weight
import data_out

def get_accel_data(data):
  return [x[0] for x in data]

def get_weight_data(data):
  return [x[1] for x in data]

data = data_in_direct.start_collection()
accel_data = get_accel_data(data)
weight_data = get_weight_data(data)
smooth_data = smooth_curve.smoothListGaussian(accel_data, 35)
peaks = find_peaks.find_peaks(smooth_data)
weight = get_weight.get_weight(weight_data)
data = { "reps": len(peaks), "weight": weight }
plt.plot(xrange(0, len(smooth_data)), smooth_data)
plt.show()
print len(peaks)
print weight
data_out.start_server(data)


