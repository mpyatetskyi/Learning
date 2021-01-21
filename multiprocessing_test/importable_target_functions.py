import multiprocessing
import worker_funcion

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker_funcion.worker)
        jobs.append(p)
        p.start()