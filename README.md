# ip2domain

### Summary
ip2domain.py will accept any file as a sysarg input when calling the script and then use regex to pull out IP addresses from the file and proceed to check the certificates of web servers at that IP for certificate names, giving you insight into websites that may be associated with the IP addresses. This will most commonly be best utilized when examining netflow data. 

Syntax: <code>python3 ip2domain.py filepath/filename.txt</code>
