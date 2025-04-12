from queue import Queue
import uuid
import random

requests = Queue()

def generate_request():
    request = {'id': uuid.uuid4(), 'subject': f'Transaction {random.randint(0, 100)}'}
    requests.put(request)


def process_requests():
    while not requests.empty():
        request = requests.get()

        print(f'Serving request {request['id']}')

    print('Requests queue is empty')


generate_request()
generate_request()
generate_request()
process_requests()
generate_request()
process_requests()