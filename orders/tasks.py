from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """Таска посылает уведомление на email, когда заказ успешно создан"""
    order = Order.objects.get(id=order_id)
    subject = f"Заказ №{order.id}"
    message = f"{order.name},\n\nВы успешно оформили заказ. Ваш номер заказа - {order.id}"

    mail_sent = send_mail(subject=subject,
                          message=message,
                          from_email='admin@myshop.com',
                          recipient_list=[order.email])

    return mail_sent
