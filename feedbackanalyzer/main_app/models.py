from django.db import models
from datetime import date
# Create your models here.

UNITS = (
    ('1', 'Unit1'),
    ('2', 'Unit2'),
    ('3', 'Unit3'),
    ('4', 'Unit4'),
)

class Deliverable(models.Model):
    date = models.DateField('deliverable Date')
    units = models.CharField(
        max_length=1,
        choices = UNITS,
        default=UNITS[0][0]
    )
    hmwname = models.CharField('homework Name', max_length=120)
    githubrepo = models.CharField('github Repository Link', max_length=120)
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.hmwname

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_units_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']