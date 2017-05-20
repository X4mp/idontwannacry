import logging
import ConfigParser
from threading import Threat

from impacket import smbserver, smb, version
from impacket.smbserver import SRVSServer

class WannaCrySMBServer(Thread):
    def __init__(self, smb2Support = False):
        Thread.__init__(self)
        self.server = 0
        self.defaultFile = None
        self.extensions = {}
	
	serverConfig = ConfigParser.ConfigParser()
	serverConfig.add_section('global')

	self.server = smbserver.SMBSERVER(('0.0.0.0',445), config_parser = smbConfig)
        self.server.processConfigFile()

# Unregistering some dangerous and unwanted commands
        self.server.unregisterSmbCommand(smb.SMB.SMB_COM_CREATE_DIRECTORY)
        self.server.unregisterSmbCommand(smb.SMB.SMB_COM_DELETE_DIRECTORY)
        self.server.unregisterSmbCommand(smb.SMB.SMB_COM_RENAME)
        self.server.unregisterSmbCommand(smb.SMB.SMB_COM_DELETE)
        self.server.unregisterSmbCommand(smb.SMB.SMB_COM_WRITE)
        self.server.unregisterSmbCommand(smb.SMB.SMB_COM_WRITE_ANDX)
# hook functions
#	 self.origsmbComNtCreateAndX = self.server.hookSmbCommand(smb.SMB.SMB_COM_NT_CREATE_ANDX, self.smbComNtCreateAndX)

	self.__srvsServer = SRVSServer()
        self.__srvsServer.daemon = True
        self.server.registerNamedPipe('srvsvc',('127.0.0.1',self.__srvsServer.getListenPort()))


