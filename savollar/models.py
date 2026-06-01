import random

from django.db import models

# Create your models here.
def generate_code():
    son = []
    for i in range(4):
        temp_code = str(random.randint(1, 9))
        son.append(temp_code)
    code = "".join(son)
    return code

class Kurs(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Kurs: {self.name}"
    
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Guruh(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Guruh: {self.name}"
    
    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"


class Savol(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='savollar')
    savol = models.CharField(max_length=200)
    
    javob_a = models.CharField(max_length=100)
    javob_b = models.CharField(max_length=100)
    javob_c = models.CharField(max_length=100)
    javob_d = models.CharField(max_length=100)
    
    ANSWER_CHOICES = [
        ('A', 'A variantı'),
        ('B', 'B variantı'),
        ('C', 'C variantı'),
        ('D', 'D variantı'),
    ]
    
    javob = models.CharField(
        max_length=1,
        choices=ANSWER_CHOICES
    )
    
    def __str__(self):
        return f"{self.kurs.name} - {self.savol[:50]}"
    
    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"




class Test_session(models.Model):
    code = models.CharField(max_length=4, unique=True, default=generate_code)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='test_sessions', null=True, blank=True)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE, related_name='test_sessions', null=True, blank=True)
    
    def __str__(self):
        return f"Test Sessiya - Kod: {self.code} ({self.kurs.name if self.kurs else 'Nomalum'})"
    
    class Meta:
        verbose_name = "Test Sessiya"
        verbose_name_plural = "Test Sessiyalar"

class Natija(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    test_session = models.ForeignKey(Test_session, on_delete=models.CASCADE, related_name='natijalar')
