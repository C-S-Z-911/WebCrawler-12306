# 12306 车票查询爬虫
> 一个基于PyQt5的12306车票查询桌面应用程序，提供直观的图形界面来查询火车票信息。

[![Python Version](https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyQt5 GUI](https://img.shields.io/badge/GUI-PyQt5-green?logo=qt&logoColor=white)](https://www.qt.io/)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

## 功能特性
- **图形化界面:** 使用PyQt5构建的用户友好界面
- **实时查询:** 支持实时查询12306车票信息
- **多站支持:** 自动处理车站名称到三字码的转换
- **完整信息展示:** 显示车次、时间、座位类型、票价等完整信息
- **错误处理:** 包含网络重试机制和错误处理

## 安装步骤
- 克隆项目:
  ```
  git clone https://github.com/C-S-Z-911/WebCrawler-12306.git
  cd WebCrawler-12306
  ```

- 安装Python依赖:
  ```
  pip install PyQt5 requests urllib3
  ```
- 或者使用pip一键安装所有依赖：
  ```
  pip install -r requirements.txt
  ```

## 使用说明
- 运行主程序文件：
  ```
  python main.py
  ```
- 或直接下载右侧发布的exe文件

## 界面操作
- **输入查询信息：**
  - 出发地: 输入出发车站名称（如：北京、上海、南京）
  - 目的地: 输入到达车站名称
  - 出发时间: 输入日期，格式为YYYY-MM-DD（如：2024-01-01）

- **执行查询：**
  - 点击"查询"按钮，程序将自动：
  - 获取最新的车站三字码
  - 向12306接口发送查询请求
  - 解析并显示车票信息

- **查看结果：**
  - 查询结果将以表格形式显示，包含以下信息：
    - 车次信息
    - 车站信息（出发站 → 到达站）
    - 时间信息（出发时间 → 到达时间）
    - 历时
    - 各种座位类型的余票情况
    - 备注信息

## UI界面
<img width="871" height="463" alt=")656W9JR5YC 5YB%}R`3HK" src="https://github.com/user-attachments/assets/bc43bfa7-8b24-42d3-9692-ccd7348a6000" />

## 核心函数说明
`threeCode()`
- 功能: 获取 12306 所有车站的三字码映射
- 返回: 字典类型，格式为 {"车站名": "三字码", ...}

`data(date, from_station, to_station)`
- 参数:
  - date: 查询日期，格式 "YYYY-MM-DD"
  - from_station: 出发站名称
  - to_station: 到达站名称
- 返回: 列车信息列表，包含详细的列车数据

## 注意事项
- **网络稳定性:** 12306 接口可能存在不稳定的情况，建议添加重试机制
- **数据格式:** 12306 接口返回的数据格式可能变更，需要定期维护
- **使用频率:** 避免高频请求，以免被服务器限制
- **车站名称:** 使用准确的车站名称，如"北京"而非"北京市"

## 故障排除
1. 查询返回"暂无数据"
    - 检查车站名称是否正确
    - 确认查询日期格式为 "YYYY-MM-DD"
    - 验证网络连接正常

2. 连接超时
    - 检查网络代理设置
    - 尝试使用重试机制
    - 更换网络环境

3. 车站代码获取失败
    - 确认 threeCode() 函数能正常访问 12306 资源
    - 检查网络防火墙设置

## 技术栈
- 前端界面：PyQt5
- 网络请求：requests
- 数据处理：JSON 解析
- 错误处理：异常捕获和重试机制
