# NPR_Assist
python爬虫爬取NPR播客节目All things considered的音频文件和转录文本

NPR的播客节目All things considered是练习英语听力的极佳材料，但目前NPR的播客服务存在以下问题：
- 网站的音频进度条极小，不方便回放反复听
- NPR One 拖动进度条时app会重新下载音频（没有本地缓存），增长了等待时间
- 其它播客APP搜索本频道没有对应的转录文本

目的是开发一款练习听力专用程序，便于回放和获取转录文本。

目前只能获取以下信息：
- 标题
- 内容类别
- 音频资源地址
- 音频时长
