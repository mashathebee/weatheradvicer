import requests

def main():
    api_key = "9ada850fd02995feb028af7aa07b1442"
    url = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
    url_formatted = url.format(city="Sydney", key=api_key)
    r = requests.get(url_formatted)
    if r.status_code != 200:
        raise Exception("Cannot access API!")

    response_dict = r.json()
    if response_dict["cod"] != 200:
        raise Exception("Cod is not 200")

    temp_calvin = response_dict["main"]["temp"]
    temp = round(temp_calvin - 273)

    if temp >= 16:
        print("Today is a nice day to go out!")
    else:
        print("Today is too cold to go out!")
