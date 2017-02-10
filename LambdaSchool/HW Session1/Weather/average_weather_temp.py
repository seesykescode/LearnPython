import requests


r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?id=5367929&units=imperial&APPID=b1754c54ae45c9eb3005124d562ae357&imperial')

data = r.json()


day_one = (data['list'][0]['temp']['day'])
day_two = (data['list'][1]['temp']['day'])
day_three = (data['list'][2]['temp']['day'])
day_four = (data['list'][3]['temp']['day'])
day_five = (data['list'][4]['temp']['day'])


average = (day_one + day_two + day_three + day_four + day_five) / 5

print('the average tempeature in the city of Long Beach for the next 5 days is ' + str(round(average)) )
