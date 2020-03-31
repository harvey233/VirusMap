import json
import requests

url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list'
province = ["河北","山西","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","台湾","内蒙古","广西","西藏","宁夏","新疆","北京","天津","上海","重庆","香港","澳门"]

def main():
    f1 = open('./data/countries.json','r',  encoding='utf-8')
    f2 = open('./data/patients.json', 'w+', encoding='utf-8')
    f2.write('[')
    data = json.loads(f1.read())

    cnt = 0
    for i in data[0].keys():
        name = data[0][i]
        params = {'country': name}
        response = requests.get(url, params=params, timeout=30)
        text = json.loads(response.text)
        if len(str(text)) == 36: continue  # 没有确诊病例
        f2.write('{\n')
        f2.write('\t"cn":"' + name + '",\n')
        f2.write('\t"en":"' + i + '",\n')
        for j in range(len(text['data'])):
            if text['data'][j]['date'][1] == '2' or text['data'][j]['date'][1] == '1':
                continue
            f2.write('\t"' + text['data'][j]['date'] + '"' + ":")
            now = text['data'][j]['confirm'] - text['data'][j]['dead'] - text['data'][j]['heal']
            f2.write('"' + str(now) + '"')
            if (j < len(text['data']) - 1): f2.write(',')
            f2.write('\n')
        f2.write('},\n')
    tot = {}
    f2.write('{\n')
    f2.write('\t"cn":"中国",\n')
    f2.write('\t"en":"China",\n')

    for i in range(len(province)):
        name = province[i]
        params = {'province': name}
        response = requests.get(url, params=params, timeout=30)
        text = json.loads(response.text)
        #print(text)
        for j in range(len(text['data'])):
            if text['data'][j]['date'][1] == '1' or text['data'][j]['date'][1] == '2': continue
            date = text['data'][j]['date']
            if date not in tot:
                tot[date] = text['data'][j]['confirm'] - text['data'][j]['heal'] - text['data'][j]['dead']
            else: tot[date] = tot[date] + text['data'][j]['confirm'] - text['data'][j]['heal'] - text['data'][j]['dead']
        #print(text)
    for i in tot.keys():
        f2.write('\t"' + i + '":"' + str(tot[i]) + '",\n')
    f2.write('}]')

main()
