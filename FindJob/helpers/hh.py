from bs4 import BeautifulSoup
import json
from threading import Thread
from FindJob.helpers.myip import get_html

# фунуция парсинга hh.ru возвращает список с вакансиями
def getData_hh(url, data):
    r = get_html(url)
    if r:
        soup = BeautifulSoup(r, 'lxml')
        try:
            vacancy_link = soup.find_all('a', class_='bloko-link HH-LinkModifier')
            company_name = soup.find('div', class_='vacancy-serp').find_all('a', class_='bloko-link bloko-link_secondary HH-AnonymousIndexAnalytics-Recommended-Company')
            city_name = soup.find('div', class_='vacancy-serp').find_all('span', class_='vacancy-serp-item__meta-info')
            public_date = soup.find('div', class_='vacancy-serp').find_all('span', class_='vacancy-serp-item__publication-date')
        except:
            return
        for i in range(len(vacancy_link)):
            vacancy = {}
            vacancy['name'] = vacancy_link[i].text.strip()
            vacancy['href'] = vacancy_link[i].get('href')
            vacancy['company'] = company_name[i].text.strip()
            vacancy['city'] = city_name[i].text.strip()
            dl = public_date[i].text.strip().split('\xa0')
            vacancy['date'] = dl[0] + ' ' + dl[1]
            vacancy['source'] = 'hh.ru'
            data.append(vacancy)

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
def getVacancy_hh(params):
    url = 'https://hh.ru/search/vacancy?st=searchVacancy?order_by=publication_time&text='+params['keywords']+'&experience='+params['experience']+'&employment='+params['employment']+'&schedule=remote&items_on_page=100'
    result = []
    i = 0
    threads = []
    # используем треды для многопоточности
    while i < 5:
        thread = Thread(target=getData_hh, args=(url, result))
        threads.append(thread)
        thread.start()
        i += 1
        url += '&page=' + str(i)
    for thread in threads:
        thread.join()
    return result

if __name__ == '__main__':
    url = 'https://hh.ru/search/vacancy?st=searchVacancy&text=Node.js&experience=doesNotMatter&employment=full&schedule=remote&items_on_page=100'
    print(getVacancy_hh(url))

