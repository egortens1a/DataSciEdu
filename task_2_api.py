import requests
import json
import sys

client_id = '5409cc8fbf7ddce4596d'
client_secret = '466024a6d80715ee6e481d25ec743dfa'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
result = {}
for id in sys.stdin:
    id = id.rstrip()
    if id == 'stop':
        break
    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)
    r.encoding = 'utf-8'
    # разбираем ответ сервера
    j = json.loads(r.text)
    result[j['sortable_name']] = int(j['birthday'])
print(*[j[0] for j in sorted(result.items(), key=lambda x: (x[1], x[0]))], sep='\n')