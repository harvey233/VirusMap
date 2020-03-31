import json

f1 = open("./data/patients.json", "r", encoding = "utf-8")

def main():
    data = json.loads(f1.read())
    for i in range(1,31):
        if i<10: date = "03.0" + str(i)
        else: date = "03." + str(i)
        dict = {"date":date}
        path = "./data/date/" + date
        f2 = open(path, "w+", encoding = 'utf-8')
        for i in range(len(data)):
            if date in data[i]:
                dict[data[i]['en']] = data[i][date]
        f2.write(str(dict).replace("'", '"'))


main()