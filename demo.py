import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/var/ftp/", perm="elr")
handler = FTPHandler
handler.authorizer = authorizer
logging.basicConfig(filename="ftp.log1",level=logging.DEBUG,format='%(asctime)s %(message)s')
server = FTPServer(("IPGOESHERE", 21), handler)
server.serve_forever()
