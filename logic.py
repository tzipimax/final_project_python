import json
from urllib.request import urlopen

def read_data():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    # store the response of URL
    response = urlopen(url)
    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())
    return data_json

def select_coins():
    data = data_json['rates']
    coins = []
    for k, v in data.items():
        coins.append(k)
    return coins

def calc_convert(value_from, value_to, coin_sum=1):
    try:
        coin_sum = float(coin_sum)
    except:
        return 'not valid sum'
    value_from = data_json['rates'].get(value_from, None)
    value_to = data_json['rates'].get(value_to, None)
    print(value_from, " ", value_to)
    if value_to and value_from:
        result = 1 / value_from * value_to * coin_sum
        write_to_log(coin_sum, result, value_from, value_to, select_date())
        return result
    return None

def select_date():
    return data_json['date']

# הוספת ההמרה לקובץ ההמרות
def write_to_log(coin_sum, result, value_from, value_to, date):
    with open('Conversions.txt', 'a') as f:
        f.write(
            f'{coin_sum} in {value_from} = {result} in {value_to}     at date: {date}\n')


data_json = read_data()