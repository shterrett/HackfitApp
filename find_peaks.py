import matplotlib.pyplot as plt
import numpy
import scipy.signal as signal
import csv
import smooth_curve as smooth

data = []

# with open('data.csv', 'rb') as f:
#   reader = csv.reader(f)
# 
#   rownum = 0
#   for row in reader:
# # Save header row.
#     if rownum == 0:
#       header = row
#       rownum += 1
#       continue
# 
#     row_item = row[3]
#     data.append(float(row_item))

print len(data)

smooth_data = smooth.smoothListGaussian(data, 50)

print signal.find_peaks_cwt(smooth_data, numpy.array(xrange(10, 20)))
plt.plot(xrange(0, len(smooth_data)), smooth_data)
plt.show()
