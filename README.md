# VirusMap

世界加油！

这是一个基于pyecharts的数据可视化项目（世界地图），集成了数据从获取、处理到可视化的模块。

数据来源于：https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list

GET 请求参数: country=(国家中文名) 或 province=(省份中文名)

如有疑问可联系：```harvey233@foxmail.com```

### 索引

```
├ VirusMap
 ├ crawler.py > patients.json ---- 爬取数据，处理后输出为文件
 ├ make.py > data/date ---- 统计某日期下各国的病例数量
 ├ main.py > outfile ---- 数据可视化
 ├ statis.py > statis.txt ---- 统计世界不同日期下的病例总数
 └ outfile<br>
     │ 0301.html ---- 某日期地图
     │ 0302.html
     │ ...
 └ data ---- 中间数据
     │ countries.json ---- ECharts支持的国家名索引
     │ patients.json ---- 世界不同日期下的病例数量(分国家)
     | provinces.json ---- 中国不同日期下的病例数量(各省累计)
     | satatis.txt ---- 世界不同日期下的病例总量
     └ date
         │ 03.01 ---- 某日期下各国的病例数量    
         │ 03.02
         │ ...   
 └ .idea ---- 工程文件
 └ venv ---- 工程文件
 ```
