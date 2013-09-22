import SocketServer
import datetime

PORTNO = 10552
TIMEOUT = 5

class InHandler(SocketServer.DatagramRequestHandler):

  def handle(self, data):
    newmsg = self.rfile.readline().rstrip()
    data = self.extract_data(newmsg, data)
    print "Client %s said ``%s''" % (self.client_address[0], data)
    self.wfile.write(self.server.oldmsg)
    self.server.oldmsg = newmsg

  def extract_data(self, msg, data):
    data_point = float(msg.split(',')[3])
    data.append(data_point)
    return data

def start_server(data):
  s = SocketServer.UDPServer(('',PORTNO), InHandler)
  print "Awaiting UDP messages on port %d" % PORTNO
  s.oldmsg = "This is the starting message."
  s.timeout = TIMEOUT
  while True:
    time = datetime.datetime.now()
    s.handle_request()
    time_2 = datetime.datetime.now()
    if (time_2 - time).total_seconds() > TIMEOUT:
      break

  print "Closed"
  print data 
  return data


