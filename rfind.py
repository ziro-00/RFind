import requests

#examples of pages to test from common.txt (/usr/share/seclist/discovery/web-web-content)
list = open("common.txt", "r")  #"r" <- modo leitura


#loop that walks trough the array and shows the stat code and the page name that is currently being tested
for item in list:
    url = "http://websitename.com" + item.replace("\n","") # .replace("\n","") <-- serve pra dar replace no "enter" do ficheiro common.txt
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print("Found: " + url)
    else:
        print("Not Found: " + url + " (" + str(resposta.status_code) + ")")
