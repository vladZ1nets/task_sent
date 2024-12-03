from celery import Celery
import os
from sqlalchemy import select
import smtplib
from email.message import EmailMessage
from database import init_db, db_session
from models import Item, Contract

# Налаштування Celery з використанням RabbitMQ як брокера
app = Celery('tasks', broker=f'amqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')

# Відключаємо результат бекенд (якщо не потрібен)
app.conf.result_backend = None

@app.task
def add(x, y):
    print(x + y)

@app.task
def send_email(contract_id):
    # Ініціалізація бази даних та отримання даних контракту
    init_db()
    contract = db_session.execute(select(Contract).filter_by(id=contract_id)).scalar()
    item = db_session.execute(select(Item).filter_by(id=contract.item)).scalar()

    # Налаштування для відправки електронної пошти
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()  # TLS для безпеки
        s.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASSWORD"))  # Логін і пароль від Gmail
        message = f"Message for item: {item.name}, Contract ID: {contract.id}"  # Повідомлення для відправки
        s.sendmail("appemail@example.com", "user1@gmail.com", message)
        s.sendmail("appemail@example.com", "user2@gmail.com", message)
        s.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
