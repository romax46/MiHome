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

    # yandex_json = json.loads(yandex_req.text)
    # print(yandex_json)
    # yandex_json['fact']['condition'] = conditions[yandex_json['fact']['condition']]
    # yandex_json['fact']['wind_dir'] = wind_dir[yandex_json['fact']['wind_dir']]
    # for parts in yandex_json['forecast']['parts']:
    #     parts['condition'] = conditions[parts['condition']]
    #     parts['wind_dir'] = wind_dir[parts['wind_dir']]
    # pogoda = dict()
    # params = ['condition', 'wind_dir', 'pressure_mm', 'humidity']
    # for parts in yandex_json['forecast']['parts']:
    #     pogoda[parts['part_name']] = dict()
    #     pogoda[parts['part_name']]['temp'] = parts['temp_avg']
    #     for param in params:
    #         pogoda[parts['part_name']][param] = parts[param]
    #
    # pogoda['fact'] = dict()
    # pogoda['fact']['temp'] = yandex_json['fact']['temp']
    # for param in params:
    #     pogoda['fact'][param] = yandex_json['fact'][param]
    # pogoda['link'] = yandex_json['info']['url']
    # print(pogoda)
    # '''  curl -vk --header "'X-Yandex-API-Key': 7bf600d2-1b84-45ec-9033-08e357c910ab" https://api.weather.yandex.ru/v2/informers/?lat=45.044029&lon=38.805221&lang=ru_RU '''
    # return pogoda


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
    in_day = in_data['day']
    in_night = in_data['night']


obj_w = weather()
weather_list(obj_w)


h = {'Headline': {'EffectiveDate': '2024-02-04T07:00:00+03:00', 'EffectiveEpochDate': 1707019200, 'Severity': 5,
                  'Text': 'Воскресенье: ожидаются ливни', 'Category': 'rain', 'EndDate': '2024-02-04T19:00:00+03:00',
                  'EndEpochDate': 1707062400,
                  'MobileLink': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?unit=c',
                  'Link': 'http://www.accuweather.com/ru/ru/yelizavyetinskaya/2431403/daily-weather-forecast/2431403?unit=c'},
     'DailyForecasts': [{'Date': '2024-01-31T07:00:00+03:00', 'EpochDate': 1706673600,
                         'Sun': {'Rise': '2024-01-31T07:47:00+03:00', 'EpochRise': 1706676420,
                                 'Set': '2024-01-31T17:31:00+03:00', 'EpochSet': 1706711460},
                         'Moon': {'Rise': '2024-01-31T23:18:00+03:00', 'EpochRise': 1706732280,
                                  'Set': '2024-02-01T10:27:00+03:00', 'EpochSet': 1706772420, 'Phase': 'WaningGibbous',
                                  'Age': 20}, 'Temperature': {'Minimum': {'Value': -4.9, 'Unit': 'C', 'UnitType': 17},
                                                              'Maximum': {'Value': 4.0, 'Unit': 'C', 'UnitType': 17}},
                         'RealFeelTemperature': {
                             'Minimum': {'Value': -5.4, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Очень холодно'},
                             'Maximum': {'Value': 2.2, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Холодно'}},
                         'RealFeelTemperatureShade': {
                             'Minimum': {'Value': -5.4, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Очень холодно'},
                             'Maximum': {'Value': 2.2, 'Unit': 'C', 'UnitType': 17, 'Phrase': 'Холодно'}},
                         'HoursOfSun': 5.0,
                         'DegreeDaySummary': {'Heating': {'Value': 18.0, 'Unit': 'C', 'UnitType': 17},
                                              'Cooling': {'Value': 0.0, 'Unit': 'C', 'UnitType': 17}},
                         'AirAndPollen': [
                             {'Name': 'AirQuality', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1,
                              'Type': 'Озон'},
                             {'Name': 'Grass', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                             {'Name': 'Mold', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                             {'Name': 'Ragweed', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                             {'Name': 'Tree', 'Value': 0, 'Category': 'Хорошая', 'CategoryValue': 1},
                             {'Name': 'UVIndex', 'Value': 2, 'Category': 'Хорошая', 'CategoryValue': 1}],
                         'Day': {'Icon': 6, 'IconPhrase': 'Преимущественно облачно', 'HasPrecipitation': False,
                                 'ShortPhrase': 'Растущая облачность', 'LongPhrase': 'Растущая облачность',
                                 'PrecipitationProbability': 3, 'ThunderstormProbability': 0, 'RainProbability': 0,
                                 'SnowProbability': 3, 'IceProbability': 0,
                                 'Wind': {'Speed': {'Value': 9.3, 'Unit': 'km/h', 'UnitType': 7},
                                          'Direction': {'Degrees': 20, 'Localized': 'ССВ', 'English': 'NNE'}},
                                 'WindGust': {'Speed': {'Value': 18.5, 'Unit': 'km/h', 'UnitType': 7},
                                              'Direction': {'Degrees': 33, 'Localized': 'ССВ', 'English': 'NNE'}},
                                 'TotalLiquid': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
                                 'Rain': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
                                 'Snow': {'Value': 0.0, 'Unit': 'cm', 'UnitType': 4},
                                 'Ice': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'HoursOfPrecipitation': 0.0,
                                 'HoursOfRain': 0.0, 'HoursOfSnow': 0.0, 'HoursOfIce': 0.0, 'CloudCover': 56,
                                 'Evapotranspiration': {'Value': 0.5, 'Unit': 'mm', 'UnitType': 3},
                                 'SolarIrradiance': {'Value': 2325.8, 'Unit': 'W/m²', 'UnitType': 33},
                                 'RelativeHumidity': {'Minimum': 63, 'Maximum': 100, 'Average': 78},
                                 'WetBulbTemperature': {'Minimum': {'Value': -7.9, 'Unit': 'C', 'UnitType': 17},
                                                        'Maximum': {'Value': 1.5, 'Unit': 'C', 'UnitType': 17},
                                                        'Average': {'Value': -2.4, 'Unit': 'C', 'UnitType': 17}},
                                 'WetBulbGlobeTemperature': {'Minimum': {'Value': -7.9, 'Unit': 'C', 'UnitType': 17},
                                                             'Maximum': {'Value': 4.0, 'Unit': 'C', 'UnitType': 17},
                                                             'Average': {'Value': -1.2, 'Unit': 'C', 'UnitType': 17}}},
                         'Night': {'Icon': 7, 'IconPhrase': 'Облачно', 'HasPrecipitation': False,
                                   'ShortPhrase': 'Облачно', 'LongPhrase': 'Облачно', 'PrecipitationProbability': 13,
                                   'ThunderstormProbability': 0, 'RainProbability': 0, 'SnowProbability': 13,
                                   'IceProbability': 0, 'Wind': {'Speed': {'Value': 9.3, 'Unit': 'km/h', 'UnitType': 7},
                                                                 'Direction': {'Degrees': 53, 'Localized': 'СВ',
                                                                               'English': 'NE'}},
                                   'WindGust': {'Speed': {'Value': 13.0, 'Unit': 'km/h', 'UnitType': 7},
                                                'Direction': {'Degrees': 33, 'Localized': 'ССВ', 'English': 'NNE'}},
                                   'TotalLiquid': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
                                   'Rain': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
                                   'Snow': {'Value': 0.0, 'Unit': 'cm', 'UnitType': 4},
                                   'Ice': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3}, 'HoursOfPrecipitation': 0.0,
                                   'HoursOfRain': 0.0, 'HoursOfSnow': 0.0, 'HoursOfIce': 0.0, 'CloudCover': 100,
                                   'Evapotranspiration': {'Value': 0.0, 'Unit': 'mm', 'UnitType': 3},
                                   'SolarIrradiance': {'Value': 0.0, 'Unit': 'W/m²', 'UnitType': 33},
                                   'RelativeHumidity': {'Minimum': 80, 'Maximum': 95, 'Average': 90},
                                   'WetBulbTemperature': {'Minimum': {'Value': -4.2, 'Unit': 'C', 'UnitType': 17},
                                                          'Maximum': {'Value': -0.7, 'Unit': 'C', 'UnitType': 17},
                                                          'Average': {'Value': -3.1, 'Unit': 'C', 'UnitType': 17}},
                                   'WetBulbGlobeTemperature': {'Minimum': {'Value': -4.0, 'Unit': 'C', 'UnitType': 17},
                                                               'Maximum': {'Value': 0.3, 'Unit': 'C', 'UnitType': 17},
                                                               'Average': {'Value': -2.7, 'Unit': 'C',
                                                                           'UnitType': 17}}},
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
