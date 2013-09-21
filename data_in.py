import SocketServer
import datetime

PORTNO = 10552
TIMEOUT = 5

class InHandler(SocketServer.DatagramRequestHandler):

  def handle(self):
    newmsg = self.rfile.readline().rstrip()
    data = self.extract_data(newmsg)
    print "Client %s said ``%s''" % (self.client_address[0], data)
    self.wfile.write(self.server.oldmsg)
    self.server.oldmsg = newmsg

  def extract_data(self, msg):
    data_list = msg.split(',')
    data_tuple = tuple([float(x) for x in data_list[1:]])
    return data_tuple

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


