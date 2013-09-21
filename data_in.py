import SocketServer

PORTNO = 10552

class handler(SocketServer.DatagramRequestHandler):

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

s = SocketServer.UDPServer(('',PORTNO), handler)
print "Awaiting UDP messages on port %d" % PORTNO
s.oldmsg = "This is the starting message."
s.serve_forever()



