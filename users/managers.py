from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phoneNumber, firstName, lastName, password):
        if not email:
            raise ValueError('پر کردن این فیلد الزامی است')

        if not phoneNumber:
            raise ValueError('پر کردن این فیلد الزامی است')

        if not firstName:
            raise ValueError('پر کردن این فیلد الزامی است')

        if not lastName:
            raise ValueError('پر کردن این فیلد الزامی است')

        user = self.model(email=email, firstName=firstName, lastName=lastName, phoneNumber=phoneNumber)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, firstName, lastName, phoneNumber, password):
        user = self.create_user(email=email, firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user