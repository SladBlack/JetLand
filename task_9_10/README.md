# First steps
1. `pip install -r requirements.txt`
2. `python manage.py migrate`

# Task 9
Число заемщиков, имеющих закрытые займы (status = closed). \
`python manage.py get_borrower_count`

# Task 10
Совокупный объем (amount) всех активных займов (status = active), принадлежащим заемщикам, 
которые зарегистрировались в 2021 году. \
`python manage.py get_amount`