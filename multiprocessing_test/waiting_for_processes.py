import multiprocessing
import time
import sys



def daemon():

    print('Starting: ', multiprocessing.current_process().name, multiprocessing.current_process().pid)
    time.sleep(2)
    print('Exiting: ', multiprocessing.current_process().name, multiprocessing.current_process().pid)

def non_daemon():
    print('Starting: ', multiprocessing.current_process().name, multiprocessing.current_process().pid)
    print('Exiting: ', multiprocessing.current_process().name, multiprocessing.current_process().pid)


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non_daemon', target=non_daemon)
    n.daemon = False

    d.start()
    #time.sleep(1)
    n.start()

    d.join(1)
    print('d.is_alive()', d.is_alive())
    n.join()