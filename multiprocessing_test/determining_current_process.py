import multiprocessing
import time


'''Passing arguments to identify or name the process
is cumbersome, and unnecessary. Each Process instance
has a name with a default value that can be changed
as the process is created. Naming processes is useful
for keeping track of them, especially in applications
with multiple types of processes running simultaneously.'''


def worker():
    name = multiprocessing.current_process().name
    print(name, ' Starting')
    time.sleep(2)
    print(name, ' Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print(name, ' Starting')
    time.sleep(2)
    print(name, ' Exiting')

if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker_1 = multiprocessing.Process(name='worker_1', target=worker)
    worker_2 = multiprocessing.Process(target=worker)

    worker_1.start()
    worker_2.start()
    service.start()


'''The debug output includes the name
of the current process on each line.
The lines with Process-3 in the name
column correspond to the unnamed
process worker_1.'''