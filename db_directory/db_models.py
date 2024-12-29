from tortoise.models import Model
import tortoise.fields


class User(Model):
    id = tortoise.fields.IntField(pk=True)
    name = tortoise.fields.CharField(max_length=100)
    email = tortoise.fields.CharField(max_length=100)
    password = tortoise.fields.CharField(max_length=100)
    user_data = tortoise.fields.JSONField(null=True)
