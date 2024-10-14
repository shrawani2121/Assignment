# Yes, by default, Django signals run in the same database transaction as the caller. This means that if the caller function is etangled inside a transaction, the receiver will also participate in that same transaction

from django.db import transaction
from django.dispatch import Signal, receiver
from django.db import connection

# Define a custom signal
my_signal = Signal()

# Variable to simulate a database-like value
db_value = {"value": 0}

# Receiver that modifies db_value
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver: Modifying db_value...")
    db_value["value"] = 1
    print(f"Receiver: db_value = {db_value['value']}")

# Function that triggers the signal inside a transaction
def process_transaction():
    global db_value
    try:
        with transaction.atomic():
            print("Starting transaction...")
            my_signal.send(sender=None)  # Trigger the signal
            print("Raising an error to rollback transaction...")
            raise Exception("Simulated error for rollback")
    except Exception as e:
        print(f"Transaction rolled back due to: {e}")
    
    print(f"After transaction: db_value = {db_value['value']}")

if __name__ == "__main__":
    process_transaction()
