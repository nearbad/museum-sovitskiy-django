from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Имя художника')
    years_of_life = models.CharField(max_length=255, blank=True, verbose_name='Даты жизни')
    bio = models.TextField(blank=True, verbose_name='Биография')
    association = models.ForeignKey('Association', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Группировка')
    education = models.ForeignKey('Education', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Образование')
    institution = models.ForeignKey('Institution', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Институция')
    exhibition = models.ForeignKey('Exhibition', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Произведение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Художник'
        verbose_name_plural = 'Художники'
        ordering = ['name']


class Association(models.Model):
    name = models.CharField(max_length=255, verbose_name='Группировка')
    content = models.TextField(verbose_name='О группировке')

    class Meta:
        verbose_name = 'Группировка'
        verbose_name_plural = 'Группировки'
        ordering = ['name']


class Education(models.Model):
    name = models.CharField(max_length=255, verbose_name='Образование')
    content = models.TextField(verbose_name='Об учреждении')

    class Meta:
        verbose_name = 'Образовательное учреждение'
        verbose_name_plural = 'Образовательные учреждения'
        ordering = ['name']


class Institution(models.Model):
    name = models.CharField(max_length=255, verbose_name='Институция')
    content = models.TextField(verbose_name='Об институции')

    class Meta:
        verbose_name = 'Институция'
        verbose_name_plural = 'Институции'
        ordering = ['name']


class Exhibition(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Произведение')
    about = models.TextField(verbose_name='О произведении')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведении'
        ordering = ['name']


class ExhibitionPhoto(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    exhibition = models.ForeignKey('Exhibition', on_delete=models.CASCADE, verbose_name='Произведение')



