import serial
import data_in
import smooth_curve
import find_peaks

# data is expected in the form of [time, x-accel, y-accel, z-accel] into 
# data-in. data_in returns a list of z-accel only.

#data = data_in.start_server()
addr  = '/dev/tty.usbmodemfd121'
baud  = 9600
fname = 'accel.csv'
fmode = 'ab'
reps  = 1000
data = []

with serial.Serial(addr,baud) as port:
    print port.readline()
    print port.readline()
    print port.readline()
    for i in range(reps):
        x = port.readline();
        vals = x.split(',');
        print vals
        data.append(vals[2]);
        #print x
        #outf.write(x)
        #outf.flush()


smooth_data = smooth_curve.smoothListGaussian(data)
peaks = find_peaks.find_peaks(smooth_data)
print peaks
