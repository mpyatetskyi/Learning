import multiprocessing_test


'''It usually more useful to be able to spawn
a process with arguments to tell it what work to do.
Unlike with threading, to pass arguments
to a multiprocessing_test Process the argument
must be able to be serialized using pickle.
This example passes each worker a number so
the output is a little more interesting.'''


def worker(num):
    print('Worker', num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing_test.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

'''The integer argument is now included
in the message printed by each worker:'''