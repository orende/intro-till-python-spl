from ftplib import FTP

ftp = FTP("ftp://localfileserver/")
ftp.login(username, passwd)

writeFn = lambda data: open("data.xml", 'wb').write(data)
ftp.retrbinary("RETR data.xml", writeFn)

ftp.quit()

