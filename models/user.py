from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100, unique=True)
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField("models.User", related_name="posts")
