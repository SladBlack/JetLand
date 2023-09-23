from django.db import models


class Borrower(models.Model):
    registration_date = models.DateField()
    inn = models.CharField(max_length=127, default='')


class Loan(models.Model):
    STATUS_CHOICES = [
        (0, 'new'),
        (1, 'active'),
        (2, 'closed'),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    issue_date = models.DateField()
    borrower = models.ForeignKey(Borrower, models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
