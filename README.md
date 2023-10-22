# Free-HLS

这是一个免费的 HLS 视频解决方案，即所谓的视频床。本项目提供一整套集成化解决方案，囊括了各环节所需的切片、转码、上传、即时分享等套件。让您可以以更方便、更低廉的方式分享您的视频到任意地方。

本项目仅供学习交流使用，在使用过程中对您或他人造成的任何损失我们概不负责。

## 服务端

执行上面指令后，访问 `http://服务器地址:33950` 若看到 Free-MyHLS 界面，表示部署成功

## 客户端

客户端，即 `up.py` 入口，提供对视频资源的切片、转码、上传的支持。可以在任意主机使用，只要您安装了必要的依赖和作出了正确的配置。

### 配置

安装最新的 Python3，以及必要包：

```bash
apt install -y ffmpeg python3 python3-pip
pip3 install requests python-dotenv
```

复制客户端配置文件 `.env.example` 为 `.env`，将 `APIURL` 改为您的服务器域名或 IP 地址，最后修改 `UPLOAD_DRIVE` 为您的 [上传驱动器](https://github.com/SakuraVincent/MyHLS/wiki/%E4%B8%8A%E4%BC%A0%E9%A9%B1%E5%8A%A8%E5%99%A8)，其值为 `uploader` 目录中的文件名。

### 开始使用

准备好目标视频文件，输入如下指令开始切片、上传：

```bash
python3 up.py test.mp4            #默认标题
python3 up.py test.mp4 测试标题    #自定义标题
python3 up.py test.mp4 测试标题 5  #自定义分段大小

python3 ls.py    #列出已上传视频
python3 ls.py 3  #列出已上传视频（第3页，50每页）
```

## 感谢
Thanks For https://github.com/sxyazi/free-hls
<br>
Thanks For https://github.com/FFmpeg/FFmpeg

## 相似服务

- [https://github.com/sxzz/free-hls.js](https://github.com/sxzz/free-hls.js)
- [https://github.com/sxzz/free-hls-live](https://github.com/sxzz/free-hls-live)
- [https://github.com/MoeClub/Note/tree/master/ffmpeg](https://github.com/MoeClub/Note/tree/master/ffmpeg)
