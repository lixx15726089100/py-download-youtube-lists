from __future__ import unicode_literals
import youtube_dl
import os
downloadlists = []


class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


ydl_opts = {
    'ignoreerrors': True,
    'writesubtitles': True,
    'writeautomaticsub': True,
    'write_all_thumbnails': True,
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': os.getcwd() + '/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    'download_archive': os.getcwd() + '/download-archive.txt',
    'logger': MyLogger(),
    # 有了已下载文件的ID记录，时间可以不用了。
    # 'daterange': '20210420,20210428'
}


with open(os.getcwd() + '/downloadlist.txt', 'r') as f:
    datas = f.readlines()

for data in datas:
    downloadlists.append(data[:-1])

print(downloadlists)

# 建立一个感兴趣的播放列表的list，然后定时运行就可以了
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(downloadlists)