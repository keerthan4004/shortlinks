import random
import string
from django.db import models

def generate_short_code():
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=6))
        if not URL.objects.filter(short_code=code).exists():
            return code

class URL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"