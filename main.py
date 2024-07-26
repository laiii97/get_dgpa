# 從www.dgpa.gov.tw取得特定縣市之停班停課狀態
import requests
from bs4 import BeautifulSoup as bs

cityList = ['基隆市','臺北市','新北市','桃園市','新竹市','新竹縣','苗栗縣','臺中市','彰化縣','雲林縣','南投縣','嘉義市','嘉義縣','臺南市','高雄市','屏東縣','宜蘭縣','花蓮縣','臺東縣','澎湖縣','連江縣','金門縣']

def get_dgpa(userInput):
    targetCity = []
    # 檢查
    if userInput == "台北市": # 是否有簡/繁問題並修正清單
        targetCity.append("臺北市")
    elif userInput == "tw": # 是否要查詢全部 (cityList)
        targetCity = cityList
    elif userInput not in cityList:
        print("錯誤: 請輸入正確的台灣縣市名")
    else:
        targetCity.append(userInput)

    website = requests.request("GET", url='https://www.dgpa.gov.tw/typh/daily/nds.html')   # 請求對象:www.dgpa.gov.tw
    website.encoding = 'utf-8'  # 防止中文亂碼
    soup = bs(website.text, 'html.parser')  # website.text為html文字檔案

    print(soup.title.text)
    updateTime = soup.find('h4').text.strip() # <h4>標籤為資料更新日期
    if len(updateTime) == 0:
        print("獲取更新時間失敗")
    else:
        print(updateTime[:21])

    table_body = soup.find('tbody', class_='Table_Body')  # 找到包含縣市資訊的tbody元素
    for trRow in table_body.find_all('tr'):
        try:
            for i in range(len(targetCity)):
                if trRow.find('td', headers='city_Name').text.strip() == targetCity[i]:
                    for tdRow in trRow.find_all('td', headers='StopWorkSchool_Info'):
                        print(" -", targetCity[i])
                        cityStatus = ""
                        for status in tdRow.find_all('font'):
                            cityStatus += status.text.strip() + "\n"
                    print("  ", cityStatus)
        except:
            pass

get_dgpa(input("輸入欲查詢的縣市:\n"))