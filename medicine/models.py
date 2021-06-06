from django.db import models

# Create your models here.
class Medicine(models.Model):
    # content = models.TextField("CONTENT")
    check_medicine = models.BooleanField(default=True)
    medicine_dt = models.DateTimeField(auto_now_add=True)


