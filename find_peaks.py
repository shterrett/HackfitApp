import numpy
import scipy.signal as signal
import csv
import smooth_curve as smooth


def find_peaks(data):
  print len(data)

  peaks = signal.find_peaks_cwt(data, numpy.array(xrange(100, 200)))
  return peaks
