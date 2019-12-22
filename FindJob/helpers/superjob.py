from bs4 import BeautifulSoup
import re
import json
from threading import Thread
from FindJob.helpers.myip import get_html

# фунуция парсинга superjob.ru возвращает список с вакансиями
def getData_sj(url, data):
    r = get_html(url)
    if r:
        soup = BeautifulSoup(r, 'lxml')
        try:
            vacancy_title = soup.find('div', class_='_1ID8B').find_all('div', class_='_3mfro CuJz5 PlM3e _2JVkc _3LJqf')
            vacancy_link = soup.find('div', class_='_1ID8B').find_all('a', class_=re.compile("icMQ_ _1QIBo"))
            company_name = soup.find('div', class_='_1ID8B').find_all('a', class_=re.compile("icMQ_ _205Zx"))
            vacancy_date = soup.find('div', class_='_1ID8B').find_all('span', class_='_3mfro _9fXTd _2JVkc _3e53o _3Ll36')
            vacancy_compensation = soup.find('div', class_='_1ID8B').find_all('span', class_=re.compile("_3mfro _2Wp8I"))
        except:
            return
        for i in range(len(vacancy_title)):
            vacancy = {}
            vacancy['name'] = vacancy_title[i].text.strip()
            vacancy['href'] = 'https://www.superjob.ru'+vacancy_link[i].get('href')
            vacancy['company'] = company_name[i].text.strip()
            vacancy['city'] = vacancy_date[i].next_sibling.next_sibling.text.strip()
            vacancy['compensation'] = vacancy_compensation[i].text.strip()
            vacancy['date'] = vacancy_date[i].text.strip()
            vacancy['source'] = 'SuperJob.ru'
            data.append(vacancy)

# главная функция, принимает на вход параметры запроса, формирует url,
# повторяет все методы 5 раз, таким образом предполагая что количество
# вакансий не больше 500
def getVacancy_sj(params, data):
    # изменим параметр в соответствии с требованием данного сайта
    if params['employment'] == 'full':
        params['employment'] = '6'
    else:
        if params['employment'] == 'part':
            params['employment'] = '10'
        else:
            params['employment'] = ''
    url = 'https://www.superjob.ru/vacancy/search/?keywords='+params['keywords']+'&remote_work=1&geo%5Bc%5D%5B0%5D=1'+'&work_type='+params['employment']
    result = []
    i = 1
    threads = []
    # используем треды для многопоточности
    while i < 10:
        thread = Thread(target=getData_sj, args=(url, data))
        threads.append(thread)
        thread.start()
        i += 1
        url += '&page=' + str(i)
    for thread in threads:
        thread.join()
    return data

if __name__ == '__main__':
    # код для проверки работы модуля
    url = 'https://www.superjob.ru/vacancy/search/?keywords=python&remote_work=1&geo%5Bc%5D%5B0%5D=1'
    getData_sj(url, [])

