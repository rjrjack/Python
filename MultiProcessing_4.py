import multiprocessing
import time


    # This illustrates the use of locks to avoid a race condition (where
    # two or more threads access and / or modify global data at the same time).

    # This is the same as MultiProcessing_3.py, except you don't have to explicitly
    # issue the lock.acquire() and lock.release() commands (see below).

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
                # Use the lock as a context manager, which will safely lock (lock.acquire()) 
                # and unlock (lock.release()) your code.
        with lock:
            number.value += 1

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
                # Use the lock as a context manager
            with lock:
                numbers[i] += 1

if __name__ == "__main__":

            # create a lock
    lock = multiprocessing.Lock()
    
    shared_number = multiprocessing.Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = multiprocessing.Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

            # pass the lock to the target function
    process1 = multiprocessing.Process(target=add_100, args=(shared_number, lock))
    process2 = multiprocessing.Process(target=add_100, args=(shared_number, lock))

    process3 = multiprocessing.Process(target=add_100_array, args=(shared_array, lock))
    process4 = multiprocessing.Process(target=add_100_array, args=(shared_array, lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')