from impacket import smbserver


server = smbserver.SimpleSMBServer()
server.addShare('Research', '~/Public', 'Research data and inovations')
server.start()
