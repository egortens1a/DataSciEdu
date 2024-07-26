import requests
import sys

for number in sys.stdin:
    res = requests.get(f'http://numbersapi.com/{int(number.rstrip())}/math?json=true')
    if res.json()['found']:
        print(res.json())
    else:
        print("Boring")
