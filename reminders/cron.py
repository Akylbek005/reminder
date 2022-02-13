import datetime

from django.core.mail import send_mail

from reminders.models import Reminders


def remind_birthday():
    today = datetime.date.today()
    week = today + datetime.timedelta(days=7)
    reminders = Reminders.objects.filter(birthday__month=week.month, birthday__day=week.day)

    message = ''

    if reminders.exists():
        for reminder in reminders:
            message += f'Через неделю у пользователея {reminder.name} день рождения! ' \
                       f'Ему исполняется {reminder.birthday.year - today.year}. ' \
                       f'Его данные {reminder.phone}, {reminder.email}\n'

        send_mail(
            subject='Happy birthday!',
            message=message,
            from_email='iakylbek005@gmai.com',
            recipient_list=['iakylbek005@gmail.com', 'admin@migrantnews.ru']
        )
