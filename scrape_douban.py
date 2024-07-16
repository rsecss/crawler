import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}

#计数器
count = 1
# 打开一个文件，准备写入数据
with open('douban_top250_movies.txt', 'w', encoding='utf-8') as file:
    for stat_num in range(0,250,25):
        url = f"https://movie.douban.com/top250?start={stat_num}"
        response = requests.get(url,headers=header)
        html = response.text
        soup = BeautifulSoup(html,"html.parser")
        # all_titiles = soup.find_all("span",attrs={"class":"title"})
        # for title in all_titiles:
        #     title_string=title.string
        #     if "/" not in title_string:
        #         print(title_string)
        all_titiles = soup.find_all("div",class_="hd")
        for title in all_titiles:
            movie_title = title.a.span.text
            print(f"{count}. {movie_title}")
            # 写入文件
            file.write(f"{count}. {movie_title}\n")
            count += 1
# 输出提示信息
print("抓取数据并保存到 douban_top250_movies.txt 文件完成。")