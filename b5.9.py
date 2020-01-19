import time

def delta_time(func):
    def wrapper():
        NUM_RUNS = 10
        avg_time = 0
        for _ in range(NUM_RUNS):
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= NUM_RUNS
        print("Выполнение заняло %.5f секунд" % avg_time)
    return wrapper

@delta_time
def fib():
    count = 0
    fib1 = fib2 = 1
    while fib1 < 4 * 10 ** 6:
        fibsum = fib1 + fib2
        fib2 = fib1
        fib1 = fibsum
        if fib1 % 2 == 0:
            count += fib1
        print('fib', fib1, 'count', count)

print(fib())