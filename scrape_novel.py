import requests
from bs4 import BeautifulSoup

# 伪装自己的请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

count = 1

# 打开文件准备写入
with open('斗破苍穹.txt','w',encoding='utf-8') as f:
    # 循环遍历指定范围页面
    for start_num in range(20980,23273,1):
        url = f'https://www.kunnu.com/doupo/{start_num}.htm' # url可以修改，这里是以该地址为例进行抓取
        
        # 发送请求并获取响应
        response = requests.get(url,headers=header)
        
        # 检查请求是否成功
        if response.status_code == 200:
            html = response.text
            
            # 使用 BeautifulSoup 解析页面
            soup = BeautifulSoup(html,"html.parser")
            
            #寻找标题并提取
            article = soup.find_all('article',class_='post clearfix')
            for content in article:
                # 提取标题并居中
                novel_title = content.header.h1.text
                centered_title = novel_title.center(60)  # 60 是总宽度，可以根据需要调整
                
                #提取文章内容
                novel_content = content.find('div',id='nr1').text
                novel_content_cleaned = novel_content.replace("鲲~弩~小~说~k u n n u - co m 💨", "") # 去除指定字符串
                
                # 打印标题和内容（可选）
                print(f'{count}. {centered_title}')
                print(novel_content_cleaned)
                print()  # 打印空行分隔每篇文章
            
            #写入文件并保存
            f.write(f'{centered_title}\n')
            f.write(f'{novel_content_cleaned}\n\n')
            count += 1

# 输出提示信息
print("抓取数据并保存到「斗破苍穹.txt」文件完成。")