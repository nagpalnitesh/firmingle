from django.core.mail import send_mail
from django.conf import settings


def send_forget_password_token(email, token):
    subject = 'Your foget password link'
    message = f'Hi, verify your account: http://127.0.0.1:8000/reset-password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
