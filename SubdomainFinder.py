import requests

url = "terra.com.br"
file = open("subs.txt")

for line in file:
    line = line.strip()

    #Monta URL
    sub_to_check = f"https://{line}.{url}"

    try:
        r = requests.get(sub_to_check)
        print("Sucesso")
        print(sub_to_check)
        print("--------------------------------")
    except:
        print(f"Não consegui {sub_to_check}")
        print("--------------------------------")
        continue