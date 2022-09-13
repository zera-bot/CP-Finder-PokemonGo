import json
import requests
import math
import csv

def getdata(txt):
	r = requests.get(txt)
	return r.text

cp_multipliers = [
    {
        "level": 1,
        "multiplier": 0.09399999678134918
    },
    {
        "level": 1.5,
        "multiplier": 0.1351374313235283
    },
    {
        "level": 2.0,
        "multiplier": 0.16639786958694458
    },
    {
        "level": 2.5,
        "multiplier": 0.1926509141921997
    },
    {
        "level": 3.0,
        "multiplier": 0.21573247015476227
    },
    {
        "level": 3.5,
        "multiplier": 0.23657265305519104
    },
    {
        "level": 4.0,
        "multiplier": 0.2557200491428375
    },
    {
        "level": 4.5,
        "multiplier": 0.27353037893772125
    },
    {
        "level": 5.0,
        "multiplier": 0.29024988412857056
    },
    {
        "level": 5.5,
        "multiplier": 0.3060573786497116
    },
    {
        "level": 6.0,
        "multiplier": 0.3210875988006592
    },
    {
        "level": 6.5,
        "multiplier": 0.33544503152370453
    },
    {
        "level": 7.0,
        "multiplier": 0.3492126762866974
    },
    {
        "level": 7.5,
        "multiplier": 0.362457737326622
    },
    {
        "level": 8.0,
        "multiplier": 0.37523558735847473
    },
    {
        "level": 8.5,
        "multiplier": 0.38759241108516856
    },
    {
        "level": 9.0,
        "multiplier": 0.39956727623939514
    },
    {
        "level": 9.5,
        "multiplier": 0.4111935495172506
    },
    {
        "level": 10.0,
        "multiplier": 0.4225000143051148
    },
    {
        "level": 10.5,
        "multiplier": 0.4329264134104144
    },
    {
        "level": 11.0,
        "multiplier": 0.443107545375824
    },
    {
        "level": 11.5,
        "multiplier": 0.4530599538719858
    },
    {
        "level": 12.0,
        "multiplier": 0.46279838681221
    },
    {
        "level": 12.5,
        "multiplier": 0.4723360780626535
    },
    {
        "level": 13.0,
        "multiplier": 0.4816849529743195
    },
    {
        "level": 13.5,
        "multiplier": 0.4908558102324605
    },
    {
        "level": 14.0,
        "multiplier": 0.4998584389686584
    },
    {
        "level": 14.5,
        "multiplier": 0.5087017565965652
    },
    {
        "level": 15.0,
        "multiplier": 0.517393946647644
    },
    {
        "level": 15.5,
        "multiplier": 0.5259425118565559
    },
    {
        "level": 16.0,
        "multiplier": 0.5343543291091919
    },
    {
        "level": 16.5,
        "multiplier": 0.5426357612013817
    },
    {
        "level": 17.0,
        "multiplier": 0.5507926940917969
    },
    {
        "level": 17.5,
        "multiplier": 0.5588305993005633
    },
    {
        "level": 18.0,
        "multiplier": 0.5667545199394226
    },
    {
        "level": 18.5,
        "multiplier": 0.574569147080183
    },
    {
        "level": 19.0,
        "multiplier": 0.5822789072990417
    },
    {
        "level": 19.5,
        "multiplier": 0.5898879119195044
    },
    {
        "level": 20.0,
        "multiplier": 0.5974000096321106
    },
    {
        "level": 20.5,
        "multiplier": 0.6048236563801765
    },
    {
        "level": 21.0,
        "multiplier": 0.6121572852134705
    },
    {
        "level": 21.5,
        "multiplier": 0.6194041110575199
    },
    {
        "level": 22.0,
        "multiplier": 0.6265671253204346
    },
    {
        "level": 22.5,
        "multiplier": 0.633649181574583
    },
    {
        "level": 23.0,
        "multiplier": 0.6406529545783997
    },
    {
        "level": 23.5,
        "multiplier": 0.6475809663534164
    },
    {
        "level": 24.0,
        "multiplier": 0.654435634613037
    },
    {
        "level": 24.5,
        "multiplier": 0.6612192690372467
    },
    {
        "level": 25.0,
        "multiplier": 0.667934000492096
    },
    {
        "level": 25.5,
        "multiplier": 0.6745819002389908
    },
    {
        "level": 26.0,
        "multiplier": 0.6811649203300476
    },
    {
        "level": 26.5,
        "multiplier": 0.6876849085092545
    },
    {
        "level": 27.0,
        "multiplier": 0.6941436529159546
    },
    {
        "level": 27.5,
        "multiplier": 0.7005428969860077
    },
    {
        "level": 28.0,
        "multiplier": 0.7068842053413391
    },
    {
        "level": 28.5,
        "multiplier": 0.7131690979003906
    },
    {
        "level": 29.0,
        "multiplier": 0.719399094581604
    },
    {
        "level": 29.5,
        "multiplier": 0.7255756109952927
    },
    {
        "level": 30.0,
        "multiplier": 0.7317000031471252
    },
    {
        "level": 30.5,
        "multiplier": 0.7347410172224045
    },
    {
        "level": 31.0,
        "multiplier": 0.7377694845199585
    },
    {
        "level": 31.5,
        "multiplier": 0.740785576403141
    },
    {
        "level": 32.0,
        "multiplier": 0.7437894344329834
    },
    {
        "level": 32.5,
        "multiplier": 0.7467812150716782
    },
    {
        "level": 33.0,
        "multiplier": 0.7497610449790955
    },
    {
        "level": 33.5,
        "multiplier": 0.7527291029691696
    },
    {
        "level": 34.0,
        "multiplier": 0.7556855082511902
    },
    {
        "level": 34.5,
        "multiplier": 0.7586303651332855
    },
    {
        "level": 35.0,
        "multiplier": 0.7615638375282288
    },
    {
        "level": 35.5,
        "multiplier": 0.7644860669970512
    },
    {
        "level": 36.0,
        "multiplier": 0.7673971652984619
    },
    {
        "level": 36.5,
        "multiplier": 0.7702972739934921
    },
    {
        "level": 37.0,
        "multiplier": 0.7731865048408508
    },
    {
        "level": 37.5,
        "multiplier": 0.7760649472475052
    },
    {
        "level": 38.0,
        "multiplier": 0.7789327502250671
    },
    {
        "level": 38.5,
        "multiplier": 0.78179006
    },
    {
        "level": 39.0,
        "multiplier": 0.78463697
    },
    {
        "level": 39.5,
        "multiplier": 0.78747358
    },
    {
        "level": 40.0,
        "multiplier": 0.79030001
    },
    {
        "level": 40.5,
        "multiplier": 0.79280001
    },
    {
        "level": 41.0,
        "multiplier": 0.79530001
    },
    {
        "level": 41.5,
        "multiplier": 0.79780001
    },
    {
        "level": 42.0,
        "multiplier": 0.8003
    },
    {
        "level": 42.5,
        "multiplier": 0.8028
    },
    {
        "level": 43.0,
        "multiplier": 0.8053
    },
    {
        "level": 43.5,
        "multiplier": 0.8078
    },
    {
        "level": 44.0,
        "multiplier": 0.81029999
    },
    {
        "level": 44.5,
        "multiplier": 0.81279999
    },
    {
        "level": 45.0,
        "multiplier": 0.81529999
    },
    {
        "level": 45.5,
        "multiplier": 0.8178
    },
    {
        "level": 46.0,
        "multiplier": 0.8203
    },
    {
        "level": 46.5,
        "multiplier": 0.8228
    },
    {
        "level": 47.0,
        "multiplier": 0.8253
    },
    {
        "level": 47.5,
        "multiplier": 0.8278
    },
    {
        "level": 48.0,
        "multiplier": 0.8303
    },
    {
        "level": 48.5,
        "multiplier": 0.8328
    },
    {
        "level": 49.0,
        "multiplier": 0.8353
    },
    {
        "level": 49.5,
        "multiplier": 0.837799
    },
    {
        "level": 50.0,
        "multiplier": 0.8403
    },
    {
        "level": 50.5,
        "multiplier": 0.84279999
    },
    {
        "level": 51.0,
        "multiplier": 0.84529999
    }]

api = 'https://pogoapi.net/api/v1/'
target = int(input("CP: "))
outputFile = input("Output Type: ") #json or csv or all

def createDictionary():
    res = json.loads(getdata(api+"pokemon_stats.json"))
    dict = {}

    for stats_ in res:
        if(stats_["form"] == "Normal"):
            pkName = stats_["pokemon_name"]
            dict[pkName] = {}
            for i in cp_multipliers:
                atk = stats_['base_attack']
                def_ = stats_['base_defense']
                sta = stats_['base_stamina']

                minCp = math.floor((atk*(def_**0.5)*(sta**0.5)*((i['multiplier'])**2))/10)
                maxCp = math.floor(((atk+15)*((def_+15)**0.5)*((sta+15)**0.5)*((i['multiplier'])**2))/10)
                if minCp < 10: minCp = 10
                if maxCp < 10: maxCp = 10

                dict[pkName][i['level']] = [minCp,maxCp,i['multiplier'],i['level'],stats_['pokemon_name']]

    with open('dict.json','w') as f:
        json.dump(dict,f)

def getPokemon(cp):
    data = None
    with open('dict.json',"r") as f:
        data = json.loads(f.read())

    res = json.loads(getdata(api+"pokemon_stats.json"))
    availableItems = []
    matches = []

    for dItem in data.values():
        for mon in dItem.values():
            if cp >= mon[0] and cp <= mon[1]:
                availableItems.append(mon)

    for mItem in availableItems:
        mon = None
        for stats_ in res:
            if stats_['pokemon_name'] == mItem[4] and stats_['form'] == "Normal":
                mon = stats_

        for x in range(16):
            for y in range(16):
                for z in range(16):
                    atk = mon['base_attack']
                    def_ = mon['base_defense']
                    sta = mon['base_stamina']
                    currentCP = math.floor(((atk+x)*((def_+y)**0.5)*((sta+z)**0.5)*((mItem[2])**2))/10)
                    if currentCP < 10: currentCP = 10

                    if currentCP == cp:
                        matches.append([mItem[4],mItem[3],x,y,z,currentCP]) #name, level, atk, def, sta, cp

    matchesLength = len(matches)
    print(matchesLength)

    if outputFile == 'all' or outputFile == 'json':
        with open('output.json','w') as f_:
            json.dump(matches,f_)

    if outputFile == 'all' or outputFile == 'csv':
        with open('output.csv', 'w', encoding='UTF8', newline='') as f__:
            writer = csv.writer(f__)
            writer.writerow(['name','level','atk','def','sta','cp'])
            if matchesLength < 1048576:
                writer.writerows(matches)

getPokemon(target)