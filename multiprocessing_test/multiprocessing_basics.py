import multiprocessing_test


'''The simplest way to spawn a second
is to instantiate a Process object with
a target function and call start() 
to let it begin working.'''


def worker():
    print('Worker')
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing_test.Process(target=worker)
        jobs.append(p)
        p.start()

'''The output includes the word “Worker”
printed five times, although it may not
be entirely clean depending on the order
of execution.'''