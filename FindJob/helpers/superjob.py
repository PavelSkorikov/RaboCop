from bs4 import BeautifulSoup
import re
import json
from threading import Thread
from FindJob.helpers.myip import get_html

# фунуция парсинга superjob.ru возвращает список с вакансиями
def get_data(url, data):
    r = get_html(url)
    if r:
        soup = BeautifulSoup(r, 'lxml')
        try:
            vacancy_title = soup.find_all('div', class_='_3mfro CuJz5 PlM3e _2JVkc _3LJqf')
            vacancy_link = soup.find_all('a', class_=re.compile("icMQ_ _1QIBo"))
            company_name = soup.find_all('a', class_=re.compile("icMQ_ _205Zx"))
            vacancy_date = soup.find_all('span', class_='_3mfro _9fXTd _2JVkc _3e53o _3Ll36')
        except:
            return
        for i in range(len(vacancy_title)):
            vacancy = {}
            vacancy['name'] = vacancy_title[i].text.strip()
            vacancy['href'] = vacancy_link[i].get('href')
            vacancy['company'] = company_name[i].text.strip()
            vacancy['city'] = vacancy_date[i].next_sibling.next_sibling.text.strip()
            vacancy['date'] = vacancy_date[i].text.strip()
            data.append(vacancy)
        print(data)

# функция записи данных в файл в формате JSON
def write_json_file(parse_data):
    try:
        data = json.load(open('vacancy.json'))
        data_result = []
        for i in parse_data:
            for j in data:
                if i not in j:
                    data_result.append(i)
        if len(data_result) != 0:
            data.append(data_result)
    except:
        data = []
        data.append(parse_data)
    with open('vacancy.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# главная функция, которая по заданному запросу  - url
# повторяет все методы 5 раз, таким образом предполагая что количество
# вакансий не больше 500
def get_vacancy(params):
    url = 'https://www.superjob.ru/vacancy/search/?keywords=python&remote_work=1&geo%5Bc%5D%5B0%5D=1'
    result = []
    i = 0
    threads = []
    # используем треды для многопоточности
    while i < 5:
        thread = Thread(target=get_data, args=(url, result))
        threads.append(thread)
        thread.start()
        i += 1
        url += '&page=' + str(i)
    for thread in threads:
        thread.join()
    return result

if __name__ == '__main__':
    url = 'https://www.superjob.ru/vacancy/search/?keywords=python&remote_work=1&geo%5Bc%5D%5B0%5D=1'
    get_data(url, [])

