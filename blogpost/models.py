from django.db import models

class SampleModel(models.Model):
    title = models.CharField(max_length = 100)
    number = models.IntegerField() #IntegerFieldは整数型のデータ

CATEGORY = (("business", "ビジネス"), ("life", "生活"), ("other", "その他"))

class BlogModel(models.Model):
    title = models.CharField(max_length = 100) #CharFieldは文字列型のデータ　#データの最大長が100である
    content = models.TextField() #
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )

    def __str__(self):
        return self.title
