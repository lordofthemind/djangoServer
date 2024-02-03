from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    date_of_birth = models.DateField()

    @classmethod
    def create_user(cls, name, email, age, date_of_birth):
        user = cls(name=name, email=email, age=age, date_of_birth=date_of_birth)
        user.save()

    @classmethod
    def get_all_users(cls):
        return cls.objects.all()

    @classmethod
    def get_user_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

    def update_user_details(cls, user_id, new_name, new_email, new_age, new_date_of_birth):
        user = cls.objects.get(pk=user_id)
        user.name = new_name
        user.email = new_email
        user.age = new_age
        user.date_of_birth = new_date_of_birth
        user.save()

    @classmethod
    def delete_user(cls, user_id):
        user = cls.objects.get(pk=user_id)
        user.delete()

    def __str__(self):
        return self.name +" "+self.email
