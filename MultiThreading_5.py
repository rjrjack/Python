import threading
import time

    # This illustrates the use of locks to avoid a race condition (where
    # two or more threads access and / or modify global data at the same time).
    
    # This is the same as MultiThreading_4.py, except you don't have to explicitly
    # issue the lock.acquire() and lock.release() commands (see below).

database_value = 0

def increase(lock):

    global database_value 
    
        # Use the lock as a context manager, which will safely lock (lock.acquire()) and unlock (lock.release()) your code.
    with lock:      
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

            # create a lock
    lock = threading.Lock()
    
    print('Start value: ', database_value)

            # pass the lock as a parameter to the target function
            
    t1 = threading.Thread(target=increase, args=(lock,))    # notice the comma after lock since args must be a tuple
    t2 = threading.Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')