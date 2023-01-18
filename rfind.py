import requests

list = open("list.txt", "r")

print('''

Built by:

███████╗██╗██████╗  ██████╗        ██████╗  ██████╗ 
╚══███╔╝██║██╔══██╗██╔═══██╗      ██╔═████╗██╔═████╗
  ███╔╝ ██║██████╔╝██║   ██║█████╗██║██╔██║██║██╔██║
 ███╔╝  ██║██╔══██╗██║   ██║╚════╝████╔╝██║████╔╝██║
███████╗██║██║  ██║╚██████╔╝      ╚██████╔╝╚██████╔╝
╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝        ╚═════╝  ╚═════╝ 
                                                    
                 ---- RFind ----
                    
    * How to use
    * Insert url: https://www.google.com/

''')

host = input("URL: ")
print("")
print("searching . . .\n")

for item in list:
    url = host + item.replace("\n","")
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print("Found: " + url)
    #else:
        #print("Not Found: " + url + " (" + str(resposta.status_code) + ")")
