import json
import requests as req
import urllib3

urllib3.disable_warnings()


def yandex_weather():
    latitude = 45.044029
    longitude = 38.805221
    token_yandex = '7bf600d2-1b84-45ec-9033-08e357c910ab'
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={latitude}&lon={longitude}&lang=ru_RU'
    url = 'https://yandex.ru/maps/?ll=38.825732%2C44.985237&mode=whatshere&utm_campaign=desktop&utm_medium=search&utm_source=maps&whatshere%5Bpoint%5D=38.805221%2C45.044029&whatshere%5Bzoom%5D=12.03&z=12'

    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': token_yandex}, verify=False)
    err = yandex_req.status_code
    print(err)
    print(yandex_req.text)
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                  'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'
                  }
    wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
                'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}


# yandex_weather()

def weather():
    code_loc = '2431403'  # Krasnodar'293686'
    api_key = 'Uzrf7CtdkbZrmI0YbjAaPoYxrIjr9DmQ'
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{code_loc}?apikey={api_key}&language=ru&details=true&metric=True'
    response = req.get(url_weather, headers={"APIKey": api_key})
    json_data = json.loads(response.text)
    print(json_data)
    # dict_weather = dict()
    # dict_weather['link'] = json_data[0]['MobileLink']
    # dict_weather['сейчас'] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    # for i in range(len(json_data)):
    #     time = 'через ' + str(i) + 'ч'
    #     dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
    # print(dict_weather)
    return json_data


def weather_list(obj):
    in_data = obj['DailyForecasts'][0]
    #in_day = in_data['day']
    #in_night = in_data['night']


obj_w = weather()
weather_list(obj_w)

h = {'Headline': {'EffectiveDate': '2024-02-05T19:00:00+03:00', 'EffectiveEpochDate': 1707148800, 'Severity': 5,
                  'Text': 'Понедельник, вечер: ожидаются ливни', 'Category': 'rain',
                  'EndDate': '2024-02-06T01:00:00+03:00', 'EndEpochDate': 1707170400,
                  'MobileLink': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?unit=c',
                  'Link': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?unit=c'},
     'DailyForecasts': [{'Date': '2024-02-05T07:00:00+03:00', 'EpochDate': 1707105600,
                         'Sun': {'Rise': '2024-02-05T07:41:00+03:00', 'EpochRise': 1707108060,
                                 'Set': '2024-02-05T17:38:00+03:00', 'EpochSet': 1707143880},
                         'Moon': {'Rise': '2024-02-05T03:55:00+03:00', 'EpochRise': 1707094500,
                                  'Set': '2024-02-05T12:13:00+03:00', 'EpochSet': 1707124380, 'Phase': 'WaningCrescent',
                                  'Age': 25}, 'Temperature': {'Minimum': {'Value': 3.0, 'Unit': 'C', 'UnitType': 17},
                                                              'Maximum': {'Value': 8.5, 'Unit': 'C', 'UnitType': 17}},
                         'RealFeelTemperature': {
                             'Minimum': {'Value': -3.2, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Холодно'},
                             'Maximum': {'Value': 4.5, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Зябко'}},
                         'RealFeelTemperatureShade': {
                             'Minimum': {'Value': -3.2, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Холодно'},
                             'Maximum': {'Value': 4.5, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Зябко'}},
                         'HoursOfSun': 1.2,
                         'DegreeDaySummary': {'Heating': {'Value': 12.0, 'Unit': 'C', 'UnitType': 17},
                                              'Cooling': {'Value': 0.0, 'Unit': 'C', 'UnitType': 17}}, 'AirAndPollen': [
             {'Name': 'AirQuality', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1, 'Type': 'Озон'},
             {'Name': 'Grass', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
             {'Name': 'Mold', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
             {'Name': 'Ragweed', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
             {'Name': 'Tree', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
             {'Name': 'UVIndex', 'Value': 1, 'Category': 'Хорошая', 'CategoryValue': 1}],
                         'Day': {'Icon': 12, 'IconPhrase': 'Ливни', 'HasPrecipitation': True,
                                 'PrecipitationType': 'Rain', 'PrecipitationIntensity': 'Moderate',
                                 'ShortPhrase': 'Ливень', 'LongPhrase': 'Ливень', 'PrecipitationProbability': 87,
                                 'ThunderstormProbability': 17, 'RainProbability': 87, 'SnowProbability': 0,
                                 'IceProbability': 0, 'Wind': {'Speed': {'Value': 22.2, 'Unit': 'km/h', 'UnitType': 7},
                                                               'Direction': {'Degrees': 245, 'Localized': 'ЗЮЗ',
                                                                             'English': 'WSW'}},
                                 'WindGust': {'Speed': {'Value': 59.3, 'Unit': 'km/h', 'UnitType': 7},
                                              'Direction': {'Degrees': 253, 'Localized': 'ЗЮЗ', 'English': 'WSW'}},
                                 'TotalLiquid': {'Value': 4.8, 'Unit': 'mm', 'UnitType': 3},
                                 'Rain': {'Value': 4.8, 'Unit': 'mm', 'UnitType': 3},
                                 'Snow': {'Value': 0.0, 'Unit': 'cm', 'UnitType': 4},
                                 'Ice': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'HoursOfPrecipitation': 1.5,
                                 'HoursOfRain': 1.5, 'HoursOfSnow': 0.0, 'HoursOfIce': 0.0, 'CloudCover': 88,
                                 'Evapotranspiration': {'Value': 0.5, 'Unit': 'mm', 'UnitType': 3},
                                 'SolarIrradiance': {'Value': 247.4, 'Unit': 'W/m²', 'UnitType': 33},
                                 'RelativeHumidity': {'Minimum': 74, 'Maximum': 88, 'Average': 83},
                                 'WetBulbTemperature': {'Minimum': {'Value': 4.6, 'Unit': 'C', 'UnitType': 17},
                                                        'Maximum': {'Value': 6.6, 'Unit': 'C', 'UnitType': 17},
                                                        'Average': {'Value': 5.8, 'Unit': 'C', 'UnitType': 17}},
                                 'WetBulbGlobeTemperature': {'Minimum': {'Value': 5.4, 'Unit': 'C', 'UnitType': 17},
                                                             'Maximum': {'Value': 8.5, 'Unit': 'C', 'UnitType': 17},
                                                             'Average': {'Value': 6.9, 'Unit': 'C', 'UnitType': 17}}},
                         'Night': {'Icon': 39, 'IconPhrase': 'Переменная облачность с дождем', 'HasPrecipitation': True,
                                   'PrecipitationType': 'Rain', 'PrecipitationIntensity': 'Moderate',
                                   'ShortPhrase': 'Ветрено', 'LongPhrase': 'Ветрено', 'PrecipitationProbability': 85,
                                   'ThunderstormProbability': 17, 'RainProbability': 85, 'SnowProbability': 0,
                                   'IceProbability': 0,
                                   'Wind': {'Speed': {'Value': 31.5, 'Unit': 'km/h', 'UnitType': 7},
                                            'Direction': {'Degrees': 262, 'Localized': 'З', 'English': 'W'}},
                                   'WindGust': {'Speed': {'Value': 66.7, 'Unit': 'km/h', 'UnitType': 7},
                                                'Direction': {'Degrees': 258, 'Localized': 'ЗЮЗ', 'English': 'WSW'}},
                                   'TotalLiquid': {'Value': 4.5, 'Unit': 'mm', 'UnitType': 3},
                                   'Rain': {'Value': 4.5, 'Unit': 'mm', 'UnitType': 3},
                                   'Snow': {'Value': 0.0, 'Unit': 'cm', 'UnitType': 4},
                                   'Ice': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'HoursOfPrecipitation': 2.0,
                                   'HoursOfRain': 2.0, 'HoursOfSnow': 0.0, 'HoursOfIce': 0.0, 'CloudCover': 68,
                                   'Evapotranspiration': {'Value': 0.3, 'Unit': 'mm', 'UnitType': 3},
                                   'SolarIrradiance': {'Value': 0.0, 'Unit': 'W/m²', 'UnitType': 33},
                                   'RelativeHumidity': {'Minimum': 77, 'Maximum': 87, 'Average': 83},
                                   'WetBulbTemperature': {'Minimum': {'Value': 3.1, 'Unit': 'C', 'UnitType': 17},
                                                          'Maximum': {'Value': 6.7, 'Unit': 'C', 'UnitType': 17},
                                                          'Average': {'Value': 5.4, 'Unit': 'C', 'UnitType': 17}},
                                   'WetBulbGlobeTemperature': {'Minimum': {'Value': 4.5, 'Unit': 'C', 'UnitType': 17},
                                                               'Maximum': {'Value': 7.6, 'Unit': 'C', 'UnitType': 17},
                                                               'Average': {'Value': 6.5, 'Unit': 'C', 'UnitType': 17}}},
                         'Sources': ['AccuWeather'],
                         'MobileLink': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?day=1&unit=c',
                         'Link': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?day=1&unit=c'}]}


u = {'Date': '2024-01-31T07:00:00+03:00', 'EpochDate': 1706673600,
     'Sun': {'Rise': '2024-01-31T07:47:00+03:00', 'EpochRise': 1706676420, 'Set': '2024-01-31T17:31:00+03:00',
             'EpochSet': 1706711460},
     'Moon': {'Rise': '2024-01-31T23:18:00+03:00', 'EpochRise': 1706732280, 'Set': '2024-02-01T10:27:00+03:00',
              'EpochSet': 1706772420, 'Phase': 'WaningGibbous', 'Age': 20},
     'Temperature': {'Minimum': {'Value': -4.9, 'Unit': 'C', 'UnitType': 17},
                     'Maximum': {'Value': 4.0, 'Unit': 'C', 'UnitType': 17}},
     'RealFeelTemperature': {'Minimum': {'Value': -5.4, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Очень холодно'},
                             'Maximum': {'Value': 2.2, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Холодно'}},
     'RealFeelTemperatureShade': {'Minimum': {'Value': -5.4, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Очень холодно'},
                                  'Maximum': {'Value': 2.2, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Холодно'}},
     'HoursOfSun': 5.0, 'DegreeDaySummary': {'Heating': {'Value': 18.0, 'Unit': 'C', 'UnitType': 17},
                                             'Cooling': {'Value': 0.0, 'Unit': 'C', 'UnitType': 17}},
     'AirAndPollen': [{'Name': 'AirQuality', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1, 'Type': 'Озон'},
                      {'Name': 'Grass', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                      {'Name': 'Mold', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                      {'Name': 'Ragweed', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                      {'Name': 'Tree', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                      {'Name': 'UVIndex', 'Value': 2, 'Category': 'Хорошая', 'CategoryValue': 1}],
     'Day': {'Icon': 6, 'IconPhrase': 'Преимущественно облачно', 'HasPrecipitation': False,
             'ShortPhrase': 'Растущая облачность', 'LongPhrase': 'Растущая облачность', 'PrecipitationProbability': 3,
             'ThunderstormProbability': 0, 'RainProbability': 0, 'SnowProbability': 3, 'IceProbability': 0,
             'Wind': {'Speed': {'Value': 9.3, 'Unit': 'km/h', 'UnitType': 7},
                      'Direction': {'Degrees': 20, 'Localized': 'ССВ', 'English': 'NNE'}},
             'WindGust': {'Speed': {'Value': 18.5, 'Unit': 'km/h', 'UnitType': 7},
                          'Direction': {'Degrees': 33, 'Localized': 'ССВ', 'English': 'NNE'}},
             'TotalLiquid': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
             'Rain': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'Snow': {'Value': 0.0, 'Unit': 'cm', 'UnitType': 4},
             'Ice': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'HoursOfPrecipitation': 0.0, 'HoursOfRain': 0.0,
             'HoursOfSnow': 0.0, 'HoursOfIce': 0.0, 'CloudCover': 56,
             'Evapotranspiration': {'Value': 0.5, 'Unit': 'mm', 'UnitType': 3},
             'SolarIrradiance': {'Value': 2325.8, 'Unit': 'W/m²', 'UnitType': 33},
             'RelativeHumidity': {'Minimum': 63, 'Maximum': 100, 'Average': 78},
             'WetBulbTemperature': {'Minimum': {'Value': -7.9, 'Unit': 'C', 'UnitType': 17},
                                    'Maximum': {'Value': 1.5, 'Unit': 'C', 'UnitType': 17},
                                    'Average': {'Value': -2.4, 'Unit': 'C', 'UnitType': 17}},
             'WetBulbGlobeTemperature': {'Minimum': {'Value': -7.9, 'Unit': 'C', 'UnitType': 17},
                                         'Maximum': {'Value': 4.0, 'Unit': 'C', 'UnitType': 17},
                                         'Average': {'Value': -1.2, 'Unit': 'C', 'UnitType': 17}}},
     'Night': {'Icon': 7, 'IconPhrase': 'Облачно', 'HasPrecipitation': False, 'ShortPhrase': 'Облачно',
               'LongPhrase': 'Облачно', 'PrecipitationProbability': 13, 'ThunderstormProbability': 0,
               'RainProbability': 0, 'SnowProbability': 13, 'IceProbability': 0,
               'Wind': {'Speed': {'Value': 9.3, 'Unit': 'km/h', 'UnitType': 7},
                        'Direction': {'Degrees': 53, 'Localized': 'СВ', 'English': 'NE'}},
               'WindGust': {'Speed': {'Value': 13.0, 'Unit': 'km/h', 'UnitType': 7},
                            'Direction': {'Degrees': 33, 'Localized': 'ССВ', 'English': 'NNE'}},
               'TotalLiquid': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
               'Rain': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'Snow': {'Value': 0.0, 'Unit': 'cm', 'UnitType': 4},
               'Ice': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'HoursOfPrecipitation': 0.0, 'HoursOfRain': 0.0,
               'HoursOfSnow': 0.0, 'HoursOfIce': 0.0, 'CloudCover': 100,
               'Evapotranspiration': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
               'SolarIrradiance': {'Value': 0.0, 'Unit': 'W/m²', 'UnitType': 33},
               'RelativeHumidity': {'Minimum': 80, 'Maximum': 95, 'Average': 90},
               'WetBulbTemperature': {'Minimum': {'Value': -4.2, 'Unit': 'C', 'UnitType': 17},
                                      'Maximum': {'Value': -0.7, 'Unit': 'C', 'UnitType': 17},
                                      'Average': {'Value': -3.1, 'Unit': 'C', 'UnitType': 17}},
               'WetBulbGlobeTemperature': {'Minimum': {'Value': -4.0, 'Unit': 'C', 'UnitType': 17},
                                           'Maximum': {'Value': 0.3, 'Unit': 'C', 'UnitType': 17},
                                           'Average': {'Value': -2.7, 'Unit': 'C', 'UnitType': 17}}},
     'Sources': ['AccuWeather'],
     'MobileLink': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?day=1&unit=c',
     'Link': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?day=1&unit=c'}


print(h['DailyForecasts'][0])
