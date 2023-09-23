import pandas as pd


def get_total_amount(file_name: str) -> int:
    """
    Get total_amount
    :param file_name: str
    :return: int
    """
    borrowers_df = pd.read_excel(file_name, sheet_name='Borrowers')
    loans_df = pd.read_excel(file_name, sheet_name='Loans')

    filtered_borrowers_df = borrowers_df[(borrowers_df['registration_date'].dt.year <= 2021)]
    filtered_loans_df = loans_df[(loans_df['rating'] <= 12)]

    merged_df = pd.merge(filtered_borrowers_df, filtered_loans_df, on='borrower_id')

    return merged_df['amount'].sum()


if __name__ == '__main__':
    result = get_total_amount(file_name='loans.xlsx')
    print(
        f'Совокупный объем всех займов с рейтингом <= 12 для компаний, '
        f'зарегистрированных в 2021 году или ранее: {result}'
    )
