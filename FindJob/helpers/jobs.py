from bs4 import BeautifulSoup
import json
from myip import get_html


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        vacancy_link = soup.find_all('a', class_='bloko-link HH-LinkModifier')
        company_name = soup.find('div', class_='vacancy-serp').find_all('a', class_='bloko-link bloko-link_secondary')
        city_name = soup.find('div', class_='vacancy-serp').find_all('span', class_='vacancy-serp-item__meta-info')
        public_date = soup.find('div', class_='vacancy-serp').find_all('span', class_='vacancy-serp-item__publication-date')
    except:
        return
    vacancy_list = []
    for i in range(len(vacancy_link)):
        vacancy = {}
        vacancy['name'] = vacancy_link[i].text.strip()
        vacancy['href'] = vacancy_link[i].get('href')
        vacancy['company'] = company_name[i].text.strip()
        vacancy['city'] = city_name[i].text.strip()
        dl = public_date[i].text.strip().split('\xa0')
        vacancy['date'] = dl[0] + ' ' + dl[1]
        vacancy_list.append(vacancy)
    return vacancy_list
def write_json_file(parse_data):
    try:
        data = json.load(open('vacancy.json'))
        data_result = []
        for i in parse_data:
            for j in data:
                if i not in j:
                    data_result.append(i)
        if len(data_result) !=0:
            data.append(data_result)
    except:
        data = []
        data.append(parse_data)
    with open('vacancy.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)




if __name__ == '__main__':
    r = get_html('https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&schedule=remote&search_period=3&text=python&specialization=15&from=cluster_professionalArea')
    try:
        write_json_file(get_data(r))
    except:
        print('сегодня ничего не найдено')