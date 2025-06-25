import random
import threading
import time
from queue import Queue

# CPU BOUND TASK EXAMPLE


ITERATIONS_CNT: int = 100_000
counter: int = 0
result_sum: int = 0


# SINGLE THREAD EXAMPLE - !!! WRONG RESULTS !!!
def do_sync_computations():
    global counter
    global result_sum

    counter += 1
    next_sum: int = result_sum + counter
    print(f"{result_sum} + {counter} = {next_sum}")
    print("-" * 20)
    result_sum = next_sum


# for i in range(ITERATIONS_CNT):
#     do_sync_computations()


# BASIC MULTITHREADING EXAMPLE


# threads = [threading.Thread(target=do_sync_computations) for _ in range(ITERATIONS_CNT)]

# # Start threads in a separate loop to allow them to run concurrently before joining
# for thread in threads:
#     thread.start()


# MULTITHREADING EXAMPLE USING LOCKS - FIXING PRINTING ISSUE

print_lock = threading.Lock()


def do_async_computations_with_print_lock():
    global counter
    global result_sum

    counter += 1
    next_sum: int = result_sum + counter

    # Use lock to ensure thread-safe access to shared resources - 'print()'

    # # Manually acquire and release the lock
    # print_lock.acquire()
    # print(f"{result_sum} + {counter} = {next_sum}")
    # print("-" * 20)
    # print_lock.release()

    # Use context manager to ensure lock is released even if an error occurs
    with print_lock:
        # This block is thread-safe
        print(f"{result_sum} + {counter} = {next_sum}")
        print("-" * 20)

    result_sum = next_sum


# threads = [
#     threading.Thread(target=do_async_computations_with_print_lock)
#     for _ in range(ITERATIONS_CNT)
# ]

# Start threads in a separate loop to allow them to run concurrently before joining
# for thread in threads:
#     thread.start()


# MULTITHREADING EXAMPLE USING LOCKS - FIXING 'result_sum' ISSUE

# Python Multithreading is preemptive, meaning that the Python interpreter can switch between threads at any time by OS scheduler.
# This can lead to race conditions, where multiple threads try to read and write shared data at the same time, leading to unpredictable results.
# # To avoid this, we can use locks to ensure that only one thread can access the shared data at a time.

computation_lock = threading.Lock()
print_lock_v_2 = threading.Lock()


def do_async_computations_with_computation_lock():
    global counter
    global result_sum

    # Use lock to ensure thread-safe access to resources shared between threads
    with computation_lock:
        previous_sum: int = result_sum
        counter += 1
        next_sum: int = result_sum + counter
        result_sum = next_sum

    # Use context manager to ensure lock is released even if an error occurs
    with print_lock_v_2:
        # This block is thread-safe
        print(f"{previous_sum} + {counter} = {next_sum}")
        print("-" * 20)


# threads = [
#     threading.Thread(target=do_async_computations_with_computation_lock)
#     for _ in range(ITERATIONS_CNT)
# ]

# Start threads in a separate loop to allow them to run concurrently before joining
# for thread in threads:
#     thread.start()

# MULTITHREADING EXAMPLE USING 'THREAD FUZZING' TECHNIQUE

# Concurrency / Thread Fuzzing - a way of testing multithreaded programs by
# randomizing the timing of thread execution — often by adding random sleep() delays —
# to increase the chance of exposing bugs like:

#   - Race conditions (two threads change shared data at the same time)
#   - Deadlocks (two threads waiting on each other forever)
#   - Data corruption or crashes


def thread_fuzzing():
    # Randomly sleep for a short time to simulate unpredictable thread execution timing
    time.sleep(random.random() * 0.1)


def do_async_computations_with_fuzzing():
    global counter
    global result_sum

    thread_fuzzing()

    # Use lock to ensure thread-safe access to resources shared between threads
    with computation_lock:
        previous_sum: int = result_sum
        counter += 1
        thread_fuzzing()
        next_sum: int = result_sum + counter
        result_sum = next_sum

    thread_fuzzing()

    # Use context manager to ensure lock is released even if an error occurs
    with print_lock_v_2:
        # This block is thread-safe
        print(f"{previous_sum} + {counter} = {next_sum}")
        print("-" * 20)

    thread_fuzzing()


# threads = [
#     threading.Thread(target=do_async_computations_with_fuzzing)
#     for _ in range(ITERATIONS_CNT)
# ]

# Start threads in a separate loop to allow them to run concurrently before joining
# for thread in threads:
#     thread.start()


# if __name__ == "__main__":
#     # Wait until all threads finished work
#     for thread in threads:
#         thread.join()

#     print(f"DONE: solution = {result_sum}")


# MULTITHREADING EXAMPLE USING QUEUES - FIXING INTERMEDIATE RESULTS PRINT ISSUE

# !!! IT'S NEVER GUARANTEED CORRECTNESS OF CALCULATION RESULTS WITH MULTITHREADING !!!

# Instead of the thread printing directly, we are to send the print output to a queue,
# and we'll have a queue watcher print out the lines one by one (FIFO)


print_queue = Queue()


def print_queue_watcher():
    while True:
        intermediate_result = print_queue.get()
        thread_fuzzing()
        print(intermediate_result)
        thread_fuzzing()
        print_queue.task_done()
        thread_fuzzing()


def do_async_computations_with_queue():
    global counter
    global result_sum

    thread_fuzzing()

    # Use lock to ensure thread-safe access to resources shared between threads
    with computation_lock:
        counter += 1
        next_sum: int = result_sum + counter

        # Instead of printing directly, put the result in the queue
        print_queue.put(f"{result_sum} + {counter} = {next_sum}")
        print_queue.put("-" * 20)

        result_sum = next_sum

    thread_fuzzing()


# if __name__ == "__main__":
#     main_threads = []

#     # Start the print watcher thread with daemon=True so it will exit when the main program exits despite being an infinite loop
#     threading.Thread(target=print_queue_watcher, daemon=True).start()

#     for _ in range(ITERATIONS_CNT):
#         main_threads.append(threading.Thread(target=do_async_computations_with_queue))

#     # Forced running the 'thread.start()' separately to add some fuzzing between starts
#     for thread in main_threads:
#         thread.start()
#         thread_fuzzing()

#     # Wait until all threads finished work
#     for thread in main_threads:
#         thread.join()

#     # Wait until all items in the print queue have been processed
#     # This ensures that all print statements are executed before the program exits
#     print_queue.join()

#     print(f"DONE: solution = {result_sum}")


# FINAL TIME OUTPUT COMPARISON BETWEEN SINGLE AND MULTITHREADING RUNS OF THE SAME TASK


def print_queue_watcher_no_fuzzing():
    while True:
        intermediate_result = print_queue.get()
        print(intermediate_result)
        print_queue.task_done()


def do_async_computations_no_fuzzing():
    global counter
    global result_sum

    # Use lock to ensure thread-safe access to resources shared between threads
    with computation_lock:
        counter += 1
        next_sum: int = result_sum + counter

        # Instead of printing directly, put the result in the queue
        print_queue.put(f"{result_sum} + {counter} = {next_sum}")
        print_queue.put("-" * 20)

        result_sum = next_sum


if __name__ == "__main__":
    # ASYNCHRONOUS TASK RUN WITH MULTITHREADING

    # Start the timer
    start_multi_time: float = time.perf_counter()

    # Start the print watcher thread with daemon=True so it will exit when the main program exits despite being an infinite loop
    threading.Thread(target=print_queue_watcher_no_fuzzing, daemon=True).start()

    threads: list = [
        threading.Thread(target=do_async_computations_no_fuzzing) for _ in range(ITERATIONS_CNT)
    ]

    # Start threads in a separate loop to ensure all are created before any start running
    for thread in threads:
        # Start the threads with some fuzzing between starts
        thread.start()

    # Wait until all threads finished work
    for thread in threads:
        thread.join()

    # Wait until all items in the print queue have been processed
    # This ensures that all print statements are executed before the program exits
    print_queue.join()

    # Stop the timer
    end_multi_time: float = time.perf_counter()

    # SYNCHRONOUS TASK RUN WITH SINGLE THREAD

    # Set the result_sum and counter to initial values
    result_sum = 0
    counter = 0

    start_sync_time: float = time.perf_counter()

    for i in range(ITERATIONS_CNT):
        do_sync_computations()

    end_sync_time: float = time.perf_counter()

    print(f"DONE: Multithreading solution = {result_sum}")
    print(f"Multithreading Elapsed time: {end_multi_time - start_multi_time:.4f} seconds")

    print(f"DONE: Single Thread solution = {result_sum}")
    print(f"Single Thread Elapsed time: {end_sync_time - start_sync_time:.4f} seconds")
