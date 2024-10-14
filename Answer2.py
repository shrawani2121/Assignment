# Yes, Django signals run in the same thread as the caller by default. This means that when a signal is triggered, the receiver executes within the same thread that initiated the signal.

import threading
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# receiver
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver is running in thread: {threading.current_thread().name}")

# Function that sends the signal
def send_signal():
    print(f"Caller function is running in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)

if __name__ == "__main__":
    send_signal()
