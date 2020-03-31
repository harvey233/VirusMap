import json
from pyecharts.charts import Map
from pyecharts import options as opts

piece = [
    {"min": 100001},
    {"min": 50001, "max": 100000},
    {"min": 25001, "max": 50000},
    {"min": 10001, "max": 25000},
    {"min": 5000, "max": 10000},
    {"min": 2501, "max": 5000},
    {"min": 1001, "max": 2500},
    {"min": 501, "max": 1000},
    {"min": 101, "max": 500},
    {"max": 100}
]

def main():
    for i in range(1,31):
        if i<10: path = "./data/date/03.0" + str(i)
        else: path = "./data/date/03." + str(i)
        print(path)
        f1 = open(path, "r", encoding = "utf-8")
        data = json.loads(f1.read())
        country = []
        number = []
        for key in data.keys():
            if key == "date": continue
            country.insert(0, key)
            number.insert(0, data[key])
        world = Map(init_opts=opts.InitOpts(width="1001px", height="460px"))
        world.add("", [list(z) for z in zip(country, number)], "world", is_map_symbol_show = False)
        world.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        world.set_global_opts(
            title_opts=opts.TitleOpts(title = "COVID-19 各国实存病例" + "\n\n2020-" + "3-" + str(i)),
            visualmap_opts=opts.VisualMapOpts(is_piecewise = True, pieces = piece),
        )
        if i<10: date = "030" + str(i)
        else: date = "03" + str(i)
        out_path = date + ".html"
        world.render(out_path)
main()