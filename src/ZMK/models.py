from django.db import models


class ZMK(models.Model):
    """
    ZMK model.
    """
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'


class RTC(models.Model):
    """
    RTC model.
    """
    zmk = models.ForeignKey(ZMK, on_delete=models.CASCADE)
    date = models.DateField()
    unloading_date = models.DateField()
    weight = models.FloatField()
    upd = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}-{self.weight}-{self.date}'

    class Meta:
        unique_together = (('zmk', 'date', 'unloading_date', 'weight'),)


class RTCObject(models.Model):
    """
    RTC object model.
    """
    rtc = models.ForeignKey(RTC, on_delete=models.CASCADE, related_name='items')
    object_weight = models.FloatField()

    def __str__(self):
        return f'{self.rtc.pk}-{self.object_weight}'
