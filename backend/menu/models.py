import uuid

from django.db import models


class LocationModel(models.Model):

    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=True)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ubereats.location <Id:{self.location_id}> <Name:{self.state}>"

    class Meta:
        db_table = "ubereats_location"
        verbose_name_plural = "Location"


class CityModel(models.Model):

    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(LocationModel, on_delete=models.RESTRICT)
    city = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=True)
    url = models.URLField(max_length=150, null=False)
    enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ubereats.city <Id:{self.city_id}> <Name:{self.city}>"

    class Meta:
        db_table = "ubereats_city"
        verbose_name_plural = "City"
        indexes = [models.indexes.Index(fields=["url"])]


class CategoryModel(models.Model):

    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=150, null=True)
    slug = models.CharField(max_length=100, null=True)
    enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ubereats.category <Id:{self.category_id}> <Name:{self.category}>"

    class Meta:
        db_table = "ubereats_category"
        verbose_name_plural = "Category"


class CityCategoryModel(models.Model):

    city_category_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    city = models.ForeignKey(CityModel, on_delete=models.RESTRICT)
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)

    def __str__(self):
        return f"ubereats.city_category <City Id:{self.city}> <Category Id:{self.category}>"

    class Meta:
        db_table = "ubereats_city_category"
        verbose_name_plural = "CityCategory"


class RestaurantModel(models.Model):

    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.ForeignKey(CityModel, on_delete=models.RESTRICT)
    restaurant = models.CharField(max_length=150, null=True, blank=True)
    restaurant_type = models.CharField(max_length=150, null=True, blank=True)
    address_locality = models.CharField(max_length=200, null=True, blank=True)
    address_region = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    address_country = models.CharField(max_length=200, null=True, blank=True)
    street_address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    rating_value = models.CharField(max_length=200, null=True, blank=True)
    review_count = models.CharField(max_length=200, null=True, blank=True)
    opening_hours = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=250, null=False)
    status = models.BooleanField(default=True)
    data = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ubereats.restaurant <Id:{self.restaurant_id}> <Name:{self.restaurant}>"

    class Meta:
        db_table = "ubereats_restaurant"
        verbose_name_plural = "restaurant"
        indexes = [models.indexes.Index(fields=["url"])]


class CategoryRestaurantModel(models.Model):

    category_restaurant_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.RESTRICT)

    def __str__(self):
        return f"ubereats.category_restaurant <Category Id:{self.category}> <restaurant Id:{self.restaurant}>"

    class Meta:
        db_table = f"ubereats_category_restaurant"
        verbose_name_plural = "Categoryrestaurant"


class MenuModel(models.Model):

    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.RESTRICT)
    menu = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(max_length=150, null=True, default=0)
    currency = models.CharField(max_length=5, null=True)
    status = models.BooleanField(default=True)
    restaurant_url = models.URLField(max_length=250, null=False)
    data = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ubereats.menu <Id:{self.menu_id}> <Name:{self.menu}>"

    class Meta:
        db_table = "ubereats_menu"
        verbose_name_plural = "menu"
