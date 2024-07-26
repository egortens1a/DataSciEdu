import requests
city = 'Kirovo-Chepetsk'
api_url = 'https://api.openweathermap.org/data/2.5/weather'#сервис с апи

params = {
    'q': city, #название города
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7', #ключ для апи (все сервисы просят ключ апи для авторизации)
    'units': 'metric' #перевод в цельсии

}

res = requests.get(api_url, params = params)
print(res.json(),sep='\n')
print()
data = res.json()
template = 'Current temperature in {} is {}'
print(template.format (city, data['main']['temp']))