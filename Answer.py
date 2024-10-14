# By default, Django signals are executed synchronously .when a signal is triggered  receiver runs immediately in the same thread as the one that sent the signal.

import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Defining Task model
class Task(models.Model):
    name = models.CharField(max_length=100)

# Creating receiver for post_save of Task model
@receiver(post_save, sender=Task)
def task_signal_receiver(sender, instance, **kwargs):
    print("Receiver: Task saved!")
    print("Receiver: Starting a time-consuming task...")
    time.sleep(3)  # Simulate a task in 3 seconds
    print("Receiver: Task completed!")

# Function that creates a new Task and triggers the signal
def create_task():
    print("Creating a new task...")
    task = Task.objects.create(name="Test Task")
    print("Task creation completed!")

if __name__ == "__main__":
    create_task()
