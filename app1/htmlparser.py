import urllib.request
from bs4 import BeautifulSoup

# my_url = 'https://github.com/SajjadKiani/fum-schedule'

def parser(my_url):

    answer = {}

    webUrl = urllib.request.urlopen(my_url)

    data = webUrl.read()

    soup = BeautifulSoup(data, 'lxml')

    try:
        link = soup.head.find('link', attrs={'rel': 'icon'})

        temp = ''

        if (link['href'].startswith('http') == False):
            if (link['href'].startswith('/') == False):
               temp = my_url + '/' + link['href']
            else:
                temp = my_url + link['href']
        else:
            temp = link['href']

        answer.update({'favicon': temp})

    except:
        # print('favicon not found!')
        pass

    try:
        des = soup.head.find('meta', attrs={'name': 'description'})
        answer.update({'description': des['content']})
    except:
        # print('description not found!')
        pass

    try:
        img = soup.head.find('meta', attrs={'property': 'og:image'})
        answer.update({"image": img['content']})
    except:
        # print("image not found!")
        pass

    return answer
