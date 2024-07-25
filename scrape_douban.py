import requests
from bs4 import BeautifulSoup

#伪装请求头
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

# 计数器
count = 1

#打开文件准备写入
with open ('douban_top250_test.txt','w',encoding='utf=8') as f:
    #遍历指定页面
    for start_number in range (0,250,25):
        url = f'https://movie.douban.com/top250?start={start_number}'

        #发送请求并获取响应
        response = requests.get(url,headers=header)
        
        if response.status_code == 200:
            html = response.text
            
            # 使用 BeautifulSoup 解析页面
            soup = BeautifulSoup(html,'html.parser')
            
            # 寻找标题并提取
            all_title = soup.find_all('div', class_='hd')
            for title in all_title:
                movie_title = title.a.span.text
                print(f'{count}. {movie_title}\n') 
                
                # 写入文件
                f.write(f'{movie_title}\n')
                count += 1
                
# 输出提示信息
print("抓取数据并保存到 douban_top250_movies.txt 文件完成。")