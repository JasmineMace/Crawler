"""
    movie
"""
import requests

import requests
import os

# 你可以调整这个范围，来下载更多的 .ts 文件
num_files = 10
base_url = "https://vip1.lz-cdn8.com/20221019/29113_c751a58c/1000k/hls/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 打开合并文件
with open('video/video.ts', 'wb') as video_file:
    for i in range(1, num_files + 1):
        ts_url = f"{base_url}df85d4c3ef30000{str(i).zfill(2)}.ts"
        response = requests.get(ts_url, headers=headers, stream=True)

        if response.status_code == 200:
            print(f"下载 {ts_url} 成功")
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)
        else:
            print(f"下载 {ts_url} 失败, 状态码: {response.status_code}")

print("所有文件下载完成！")
