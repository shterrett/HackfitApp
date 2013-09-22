import data_in
import smooth_curve
import find_peaks

# data is expected in the form of [time, x-accel, y-accel, z-accel] into 
# data-in. data_in returns a list of z-accel only.
data = data_in.start_server()
smooth_data = smooth_curve.smoothListGaussian(data)
peaks = find_peaks.find_peaks(smooth_data)
print peaks
