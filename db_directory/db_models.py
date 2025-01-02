from tortoise.models import Model
import tortoise.fields


class User(Model):
    id = tortoise.fields.IntField(pk=True)
    name = tortoise.fields.CharField(max_length=100)
    email = tortoise.fields.CharField(unique=True, max_length=100)
    password = tortoise.fields.CharField(max_length=100)
    birthdate = tortoise.fields.DateField()
    orders = tortoise.fields.JSONField(null=True)
    session_id = tortoise.fields.CharField(null=True, max_length=200)
    created_at = tortoise.fields.DatetimeField(auto_now_add=True)
    updated_at = tortoise.fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f'User id: {self.id}, user name: {self.name}'

    def __repr__(self):
        return f'User id: {self.id}, user name: {self.name}'


class Product(Model):
    id = tortoise.fields.IntField(pk=True)
    name = tortoise.fields.CharField(max_length=100)
    description = tortoise.fields.TextField()
    price = tortoise.fields.FloatField()
    in_stock = tortoise.fields.IntField()
    gender = tortoise.fields.CharField(max_length=100)
    sizes_in_stock = tortoise.fields.JSONField()
    img_path = tortoise.fields.CharField(max_length=200)

    def __str__(self):
        return f'Product id: {self.id}, product name: {self.name}'

    def __repr__(self):
        return f'Product id: {self.id}, product name: {self.name}'
