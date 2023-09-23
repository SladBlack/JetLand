from django.core.management.base import BaseCommand
from db.models import Borrower, Loan


class Command(BaseCommand):
    def handle(self, *args, **options):
        borrower_count = Borrower.objects.filter(
            loans__status=Loan.STATUS_CHOICES[2][0]
        ).count()
        print(f'Число заемщиков, имеющих закрытые займы: {borrower_count}')
