import data_in
import smooth_curve
import find_peaks

data = []
data = data_in.start_server(data)
data = smooth_curve.smoothListGaussian(data)
peaks = find_peaks.find_peaks(data)
print peaks
