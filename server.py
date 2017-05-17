from impacket import smbserver


server = SimpleSMBServer()
server.addShare('Research', '~/Public', 'Research data and inovations')
server.start()
