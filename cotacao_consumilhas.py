import urllib.request

url = "https://github.com/jennimotaa/Consumilhas_rastreio/blob/main/cotacao_consumilhas.py"
exec(urllib.request.urlopen(url).read().decode('utf-8'))
