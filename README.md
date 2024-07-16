# Crawler(python)

由于想要提高获取数据的能力，我最近花了几天学习了pyhon的基础语法，并且通过学习相关的爬虫基础操作(应该满足我的日常的爬虫需求)，然后经行一个爬虫想项目的练习，将记录我后面相关的爬虫项目记录

## 爬虫练习

[github上面发现的收集各种免费的Python爬虫项目](https://github.com/ityard/python-fxxk-spider)

### 我的练习

1. [豆瓣抓取电影排名TOP25](scrape_douban.py)

## 爬虫注意事项

[github上面发现的中国爬虫违法违规案例汇总](https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China)

### 爬虫的原则

1. Robots.txt 文件：
Robots.txt 是网站根目录下的一个文本文件，用于指示搜索引擎和爬虫程序哪些页面可以访问，哪些页面不应该访问。
如果网站的 Robots.txt 文件明确允许爬虫访问某些页面，那么你通常可以爬取这些页面。
但是，请注意，Robots.txt 只是一个建议，不是强制性规定。一些爬虫可能会忽略 Robots.txt，或者网站可能会有其他防爬虫措施。

2. 网站的服务条款和法律条款：
有些网站在其服务条款或法律声明中明确禁止使用自动化工具进行数据采集。
在爬取网站数据之前，应该先阅读和理解网站的服务条款及法律声明，确保不会违反其规定。

3. 频率和请求量的控制：
合理的爬取频率和请求量对于网站的服务器负载和稳定性非常重要。
如果你的爬虫程序过于频繁地访问同一个网站，可能会对网站造成负担，甚至被视为恶意行为。

4. 无害性原则：
爬虫应该遵循无害性原则，不应对网站造成负面影响，如破坏性爬取、大量下载等。

5. 反爬虫措施：
一些网站会采取技术措施来防止爬虫访问，如验证码、IP封锁、动态页面加载等。
在爬取网站之前，需要了解并适应这些反爬虫措施，确保能够有效地获取数据。

### 获取robots.txt的方法

1. 网站根目录访问：
Robots.txt 文件通常位于网站的根目录下。例如，如果要查看 `https://www.example.com` 的 Robots.txt 文件，你可以访问`https://www.example.com/robots.txt`。

2. 直接访问方式：
直接在浏览器中输入网址后面加上 /robots.txt，例如 `https://www.example.com/robots.txt`，然后回车即可访问。

3. 通过命令行或工具访问：
你也可以使用命令行工具如 curl 或者 wget 来获取 Robots.txt 文件。例如，在命令行中输入：
`curl https://www.example.com/robots.txt`
或者
`wget https://www.example.com/robots.txt`

4. 查看内容：
访问到 Robots.txt 文件后，可以直接查看其中的内容。这些内容通常是针对搜索引擎和爬虫程序的规则和指南，告诉它们哪些页面可以访问，哪些页面不应该访问。
5. 解读内容：
Robots.txt 文件中的内容可以包含多条规则，每条规则通常有两个主要部分：User-agent 和 Disallow。User-agent 指定了规则适用的爬虫程序，而 Disallow 则指定了该爬虫程序不能访问的路径。

6. 注意事项：
   - 遵守 Robots.txt 规则：虽然 Robots.txt 提供了指导性的规则，但并不是所有的爬虫都会严格遵守。有些爬虫可能会忽略 Robots.txt 文件的指示。
   - 不一定存在：并非所有的网站都有 Robots.txt 文件，或者该文件可能只包含少量信息。
