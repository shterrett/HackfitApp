import serial

addr  = '/dev/tty.usbmodem1411'
baud  = 9600
fname = 'accel.csv'
fmode = 'ab'
reps  = 600

def start_collection():
  data = []

  with serial.Serial(addr,baud) as port:
      print port.readline()
      print port.readline()
      print port.readline()
      for i in range(reps):
          x = port.readline();
          vals = x.split(',');
          print vals
          data.append((float(vals[2]), float(vals[3])));
          #print x
          #outf.write(x)
          #outf.flush()
  return data


