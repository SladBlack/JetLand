from typing import Union

import requests
from settings import TOKEN, API_URL


def get_total_amount(data: dict) -> Union[None, int]:
    """
    Get total investor income for the 4th quarter of 2022
    :param data: dict
    :return:
    """
    result = 0
    borrowers = data.get('Заемщики')
    if not borrowers:
        return

    for borrower in borrowers:
        agreements = borrower.get('ДоговораЗаймов')
        if not agreements:
            continue

        for agreement in agreements:
            date = agreement.get('ДатаДоговора')
            if not date:
                continue

            if not '2022-10-01' <= date < '2023-01-01':
                continue

            income_list = agreement.get('Доходы')
            if not income_list:
                continue

            result += sum(x['Сумма'] for x in income_list)

    return round(result)


# Необходимо найти совокупный доход инвесторов за 4 квартал 2022 (по всем займам)
if __name__ == '__main__':
    response = requests.get(
        url=API_URL,
        headers={
            'Authorization': f'Token {TOKEN}'
        }
    )
    total_amount = get_total_amount(data=response.json())
    print(f'Совокупный доход инвесторов за 4 квартал 2022 (по всем займам): {total_amount}')
