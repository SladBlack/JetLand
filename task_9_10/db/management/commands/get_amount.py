from django.core.management.base import BaseCommand
from db.models import Borrower, Loan
from django.db.models import Sum


# Для базы данных из предыдущей задачи найдите совокупный объем (amount) всех активных займов (status = active),
# принадлежащим заемщикам, которые зарегистрировались в 2021 году. В ответе необходимо указать совокупный объем.
class Command(BaseCommand):
    def handle(self, *args, **options):
        query = Loan.objects.filter(
            status=Loan.STATUS_CHOICES[1][0],
            borrower__registration_date__year=2021,
        ).aggregate(
            total_amount=Sum('amount')
        )
        print(f'Совокупный объем: {query["total_amount"]}')
