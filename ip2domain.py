#Syntax: python3 new2.py filepath/augurynetflowfile
import socket
import ssl
import OpenSSL.crypto as crypto
import sys
import re



f = open(sys.argv[1],'r')
text = f.read()
ips = [] 
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)

for ip in ips:
    try:
        dst = (ip,443)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect(dst)

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = ctx.wrap_socket(s, server_hostname=dst[0])

        # get certificate
        cert_bin = s.getpeercert(True)
        x509 = crypto.load_certificate(crypto.FILETYPE_ASN1,cert_bin)
        print("IP: " +str(ip) + " || Cert name: "+ x509.get_subject().CN)
    except socket.error:
        print("IP: " +str(ip) + " || No cert")
        continue
    else:
        continue