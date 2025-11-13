import requests
import re
import time
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def threeCode():
    # 获取站点对应三字码
    code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }

    request = requests.get(code_url, headers=header)
    code_data = request.text
    # print(code_data)
    code_data = code_data[20:]
    #print(code_data)
    list_code = code_data.split("|")
    #print(list_code)
    a=1
    b=2
    t1=[]
    t2=[]
    while (a < (len(list_code))):
        t1.append(list_code[a])
        t2.append(list_code[b])
        a = a + 5
        b = b + 5
    dic = dict(zip(t1,t2))
    return dic

def data(date, from_station, to_station):
    code = threeCode()
    if not code:
        print("无法获取车站代码")
        return [["暂无数据" for _ in range(57)]]

    from_code = code.get(from_station)
    to_code = code.get(to_station)

    if not from_code or not to_code:
        print(f"未找到车站代码: {from_station}={from_code}, {to_station}={to_code}")
        return [["暂无数据" for _ in range(57)]]

    url = f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={from_code}&leftTicketDTO.to_station={to_code}&purpose_codes=ADULT"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc",
        "X-Requested-With": "XMLHttpRequest"
    }

    session = requests_retry_session()

    try:
        # 初始化会话
        init_response = session.get("https://kyfw.12306.cn/otn/leftTicket/init", headers=headers, timeout=10)
        time.sleep(0.5)

        # 获取数据
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        result = response.json()
        if result.get("httpstatus") != 200:
            print(f"API返回错误: {result.get('messages', ['未知错误'])}")
            return [["暂无数据" for _ in range(57)]]

        data = []
        if not result["data"]["result"]:
            print(f"获取车票数据为空")
            return [["暂无数据" for _ in range(57)]]
        for item in result["data"]["result"]:
            txt = re.split(r'\|', item)
            # 转换车站代码为车站名
            for b in range(6, 8):
                if b < len(txt) and txt[b]:
                    txt[b] = result["data"]["map"].get(txt[b], txt[b])
            data.append(txt)

        return data

    except Exception as e:
        print(f"获取车票数据失败: {e}")
        return [["暂无数据" for _ in range(57)]]


if __name__ == "__main__":
    result = data("2025-11-14", "南京", "武汉")
    for train in result:
        print(train)

