from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    help = 'Создать суперпользователя'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@mail.ru',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123456789qwerty')
        user.save()
