#從www.dgpa.gov.tw取得特定縣市之停班停課狀態
import requests
from bs4 import BeautifulSoup as bs

def get_dgpa(targetCity):
    cityList = {'基隆市':'city_Name Keelung City','台北市':'city_Name Taipei City','臺北市':'city_Name Taipei City','新北市':'city_Name New Taipei City','桃園市':'city_Name Taoyuan City','新竹市':'city_Name Hsinchu City','新竹縣':'city_Name Hsinchu County','苗栗縣':'city_Name Miaoli County','臺中市':'city_Name Taichung City','彰化縣':'city_Name Changhua County','雲林縣':'city_Name Yunlin County','南投縣':'city_Name Nantou county','嘉義市':'city_Name Chiayi City','嘉義縣':'city_Name Chiayi County','臺南市':'city_Name Tainan City','高雄市':'city_Name Kaohsiung City','屏東縣':'city_Name Pingtung County','宜蘭縣':'city_Name Yilan County','花蓮縣':'city_Name Hualien County','臺東縣':'city_Name Taitung County','澎湖縣':'city_Name Penghu County','連江縣':'city_Name Lienchiang County','金門縣':'city_Name Kinmen County'}

    while True:
        if targetCity in cityList:
            targetCity = cityList[targetCity]
            break
        else:
            print("找不到該縣市, 請嘗試輸入完整縣市名稱 ex:新竹縣")
            targetCity = input("輸入欲搜尋的縣市: ")
    
    website = requests.request("GET", url='https://www.dgpa.gov.tw/')   #請求對象:www.dgpa.gov.tw
    website.encoding = 'utf-8'  #防止中文亂碼
    soup = bs(website.text, 'html.parser')  #website.text為html文字檔案

    print(soup.title.text)
    updateTime = soup.find('h4').text.strip() #<h4>標籤為資料更新日期
    if len(updateTime) == 0:
        print("獲取更新時間失敗")
    else:
        print(updateTime)

    table_body = soup.find('tbody', class_='Table_Body')  #找到包含縣市資訊的tbody元素
    for trRow in table_body.find_all('tr'):
        if trRow.find('td', headers=targetCity):
            cityName = trRow.find('font').text.strip()
            cityStatus = trRow.find('td', width='70%').text.strip()
            print(cityName, cityStatus)

get_dgpa(input("輸入欲搜尋的縣市: "))