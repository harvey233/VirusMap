import json

tot = 0
def main():
    f0 = open('./data/statis.txt', 'w', encoding = 'utf-8')
    for i in range(1,31):
        tot = 0
        if i<10: path = './data/date/03.0' + str(i)
        else: path = './data/date/03.' + str(i)
        f1 = open(path, 'r', encoding = 'utf-8')
        data = json.loads(f1.read())
        for j in data.keys():
            if j == 'date': continue
            tot = tot + int(data[j])
        f0.write(path[13:] + ' : ' + str(tot) + '\n')


main()