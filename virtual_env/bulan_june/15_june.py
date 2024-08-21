import time

def f(x):
    time.sleep(3)
    return x*x

if __name__=='__main__':
    t_awal = time.perf_counter()
    futures = [f.i for i in range(5)]

    print(futures)