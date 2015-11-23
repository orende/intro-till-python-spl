import smtplib

server = smtplib.SMTP('localhost')
fromaddr = "noreply@company.com"
toaddrs = ["IT_DEPT@company.com"]
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
msg = msg + "Nya VIP kunder har importerats"
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

