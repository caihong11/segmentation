import csv
import time
import requests


def get_result(gid):
    url = f'https://napi-huawei.tianyancha.com/services/v3/t/common/baseinfoV5/{gid}.json?_=1705627726959'
    # print(url)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Referer': 'https://www.tianyancha.com/',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'Version': 'TYC-Web',
        'X-Auth-Token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTMxNTE3ODE4NSIsImlhdCI6MTcwNTYyNzQwMCwiZXhwIjoxNzA4MjE5NDAwfQ.iPyXaofR8zq3wD36ZARbN9iXSRhlbPSv810seRwhU97iI4iJjfwbPTambaryYokmPnGYSvf3yC1pezJGxt-Xrw',
        'X-Tycid': '3c635c30b66911eeaaaf51daac81f7e1'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        return
    json_dict = response.json()
    # print(json_dict)
    state = json_dict.get('state')
    if state != 'ok':
        return ''
    auctions = json_dict.get('data')
    # print(auctions)
    if not auctions:
        return

    type_1 = auctions.get('type', '')
    name_1 = auctions.get('name', '')
    person_name = auctions.get('legalPersonName')
    reg_Capital = auctions.get('regCapital')
    registration_DateStr = auctions.get('registrationDateStr')
    reg_Status = auctions.get('regStatus')
    reg_Institute = auctions.get('regInstitute')
    business_Unit = auctions.get('businessUnit')
    registration_Number = auctions.get('registrationNumber')
    types_1 = auctions.get('types')
    Credit_Code = auctions.get('creditCode')
    expiry_date = auctions.get('expiryDate')
    tax_Address = auctions.get('taxAddress')
    business_Scope = auctions.get('businessScope')

    with open('信息.csv', 'a', newline='', encoding='utf-8-sig') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(
            [type_1, name_1, person_name, reg_Capital, registration_DateStr, reg_Status, reg_Institute, business_Unit, registration_Number, types_1, Credit_Code, expiry_date, tax_Address, business_Scope]
        )
    time.sleep(2)


if __name__ == '__main__':
    with open('/home/logos/data/gs/base_info_8.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            gid = row[0]
            data = get_result(gid)
            print(data)

