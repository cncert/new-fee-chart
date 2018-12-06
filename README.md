# 话费地图

![截图](./assets/images/screenshot/xx)

### 项目说明

本项目主要目的是直观列出北京的话费营业厅

**项目网址：** [https://](https://)

**数据版权：** [CC 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

### 针对开发者的说明

#### 安装步骤

``` bash
npm install
npm run dev
npm run build
```

通过 [http://127.0.0.1:8080](http://127.0.0.1:8080) 访问

#### 网站使用技术栈

- *JS 框架:* [Vue2.js](https://cn.vuejs.org/)
- *CSS 框架:* [Bulma.io](http://bulma.io/)
- *Ajax:* [axios](https://github.com/axios/axios) 
- *地图:* [Leaflet.js](http://leafletjs.com/)
- *搜索:* [Bloodhound.js](https://github.com/twitter/typeahead.js/blob/master/doc/bloodhound.md)

#### 数据加载与解析

网页在加载时，会异步请求一次 [GeoJson](http://geojson.org/) 数据，然后包括地图、搜索框、sidebar 均使用该数据进行解析和加载。

[地图数据] 是由 [Python 脚本](/assets/script/csv2geojson.py) 通过 [CSV文件](/assets/data/hospital.csv) 生成，[CSV文件](/assets/data/hospital.csv) 中包含了 高德地图 和 Google 地图的 MapID，可以在未来做更多的功能开发。
