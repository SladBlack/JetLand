import pandas as pd


def get_borrowers_count(file_name: str) -> int:
    df = pd.read_excel(file_name, sheet_name='Borrowers')
    filtered_df = df[(df['registration_date'].dt.year == 2021) & (df['inn'] % 10 == 0)]
    return len(filtered_df)


if __name__ == '__main__':
    result = get_borrowers_count(file_name='loans.xlsx')
    print(f"Количество заемщиков, удовлетворяющих условиям: {result}")
