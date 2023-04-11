from celery import shared_task
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT
from .models import Order


@shared_task
def order_created(order_id):
    """Таска посылает уведомление на email, когда заказ успешно создан"""
    order = Order.objects.get(id=order_id)

    sender = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD
    server = smtplib.SMTP_SSL(f'{EMAIL_HOST}: {EMAIL_PORT}')

    msg = MIMEMultipart()
    msg['Subject'] = f"Заказ №{order.id}"
    msg['From'] = 'Euphoria Cakeshop <' + sender + '>'
    msg['To'] = order.email
    msg['Reply-To'] = sender

    msg_body = MIMEText(f"{order.name},\n\nВы успешно оформили заказ. Ваш номер заказа - {order.id}",
                        'plain')

    msg.attach(msg_body)

    try:
        server.login(user=sender, password=password)
        mail_sent = server.sendmail(from_addr=sender, to_addrs=order.email, msg=msg.as_string())
        print('The message was sent successfully!')
        return mail_sent
    except Exception as e:
        return f'{e}\nПроверьте ваш логин и пароль.'


