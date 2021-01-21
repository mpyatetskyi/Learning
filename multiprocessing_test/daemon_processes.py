import multiprocessing
import sys
import time


'''By default the main program will not exit
until all of the children have exited.
There are times when starting a background
process that runs without blocking the main
program from exiting is useful, such as in
services where there may not be an easy way
to interrupt the worker, or where letting it
die in the middle of its work does not lose
or corrupt data (for example, a task that generates
“heart beats” for a service monitoring tool).

To mark a process as a daemon, set its daemon
attribute with a boolean value.
The default is for processes to not be daemons,
so passing True turns the daemon mode on.'''


def daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non_daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

'''The output does not include the “Exiting” message
from the daemon process, since all of the non-daemon
processes (including the main program)
exit before the daemon process wakes up
from its 2 second sleep.'''

'''The daemon process is terminated automatically
before the main program exits, to avoid leaving
orphaned processes running. You can verify this
by looking for the process id value printed when
you run the program, and then checking for that
process with a command like ps.'''