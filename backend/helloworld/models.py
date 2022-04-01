from django.db import models

# Create your models here.
class BusinessData(models.Model):
    business_name = models.CharField(
        max_length = 20,
        help_text= "Business title",
        null = false,
    )
    business_price = models.CharField(
        max_length = 20,
        help_text= "Business price",
        null = false,
    )
    business_rating = models.CharField(
        max_length = 20,
        help_text= "Business rating",
        null = false,
    )
    business_distance = models.CharField(
        max_length = 20,
        help_text= "Business Distnace",
        null = false,
    )
    business_location = models.CharField(
        max_length = 20,
        help_text= "Business title",
        null = false,
    )

    def_str_(self):
        return self.businessData

class MenuItem(models.Model):
    Item = models.ImageField(
        upload_to = None, 
        height_field = None,
        width_field = None, 
        max_length = 100,

        )

    item_price = models.CharField(
        max_length = 20,
        help_text= "Item Price",
        null = true,
        blank = true,
    )
    business_that_makes_it = models.ForeignKey(
        BusinessData,
        on_delete = models.CASCADE
        )

