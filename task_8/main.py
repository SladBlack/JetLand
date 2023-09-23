import requests
from bs4 import BeautifulSoup


def get_tags_count(src_url: str) -> int:
    """
    Get count of tags with attributes
    :param src_url: str
    :return:int
    """
    response = requests.get(src_url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(lambda tag: len(tag.attrs) > 0)
    return len(tags)


if __name__ == '__main__':
    print(get_tags_count(src_url='https://jetlend.ru/wp-content/uploads/jetlend.html'))
