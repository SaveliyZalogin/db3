from django.db import models

Male = 'Male'
Female = 'Female'
choises = {(Male, 'Male'),
            (Female, 'Female')}


class Key_word(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_word = models.CharField(max_length=100)

    def __str__(self):

        return f'{self.id} {self.key_word}'


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=False)
    ava = models.ImageField(upload_to="static/images", blank=True)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=choises, default=Male)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} '


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_annotation = models.CharField(max_length=200)
    post_text = models.TextField()
    key_words = models.ManyToManyField(Key_word, blank=True)
    post_image = models.ImageField(upload_to="static/images", verbose_name='photo', blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, default='N   one')

    def __str__(self):
        return f'{self.id} {self.post_title}'



