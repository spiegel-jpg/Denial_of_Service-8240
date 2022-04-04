from datetime import datetime
d1 = datetime.strptime("19/Dec/2020:13:57:26 +0100", "%d/%b/%Y:%H:%M:%S %z")
d2 = datetime.strptime("22/Mar/2022:20:36:19 +0100", "%d/%b/%Y:%H:%M:%S %z")
H=(d2.timestamp()-d1.timestamp())/3600
print(H)
# Row(remote_host=IPv4Address('81.174.152.222'), ident=None, remote_user=None, time=DateTime(2020, 6, 30, 23, 38, 3), request=Request(method='GET', url=Url(scheme='', netloc='', path_str='/', params='', query_str='', fragment=''), protocol='HTTP/1.1'), status=200, size=6763)
