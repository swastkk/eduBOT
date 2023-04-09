from django.db import models

# Create your models here.

class Learnit(models.Model):
    OP_LENGTH= [
        ("100", "100"),
        ("150", "150"),
        ("200", "200"),
        ("250", "250"),
        ("300", "300"),
        ("350", "350"),
        ("400", "400"),
    ]
    question = models.TextField(blank= False, null= True)
    op_length= models.CharField(max_length=1, choices= OP_LENGTH)

    
