import numpy
import scipy.signal as signal
import csv
import smooth_curve as smooth


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
def find_peaks(data):
  print len(data)

  smooth_data = smooth.smoothListGaussian(data, 50)

  print signal.find_peaks_cwt(smooth_data, numpy.array(xrange(10, 20)))
