from queue import Queue
from faker import Faker
import time

q = Queue(maxsize=5)
fake = Faker()


def generete_request(request):
    if q.full():
        return "The queue is full"
    else:
        q.put(request)
        return f"Request {request} added to the queue"


def process_request():
    if q.empty():
        return "The queue is empty"
    else:
        while not q.empty():
            print(f"Processing request {q.get()}")
            time.sleep(1)
            print(f"Request done\n")
        return "All requests have been processed"


def main():
    while True:
        if generete_request(fake.name()) == "The queue is full":
            break
        else:
            generete_request(fake.name())
    print(process_request())


if __name__ == "__main__":
    main()
