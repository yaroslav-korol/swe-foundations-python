import time
from concurrent import futures

start: float = time.perf_counter()


def imitate_io_job(sec: float):
    print("Start doing some work")
    time.sleep(sec)
    return f"Finished work in seconds: {sec}"


# Synchronous task run

# for _ in range(3):
#     imitate_io_job(1.5)

# print(f"Total time of all SYNCHRONOUS jobs run: {time.perf_counter() - start}")


# ASYNCHRONOUS TASK RUN


# USING THREADING


# Manual step-by-step approach

# import threading

# # Initiate threads
# thread_1 = threading.Thread(target=imitate_io_job, args=[1.5])
# thread_2 = threading.Thread(target=imitate_io_job, args=[1.5])

# # Start thread run
# thread_1.start()
# thread_2.start()

# # Make sure / wait until thread finished work
# thread_1.join()
# thread_2.join()


# print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start}")


# # Multiple threads generator
# threads: list = []

# for _ in range(10):
#     thread = threading.Thread(target=imitate_io_job, args=[1.5])
#     thread.start()
#     threads.append(thread)

# # Wait until all threads finished work
# for t in threads:
#     t.join()


# print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start}")


# USING CONCURRENT FUTURES

# # Manual step-by-step approach

# # Create future objects with 'executor' context manager
# with futures.ThreadPoolExecutor() as executor:
#     t_1 = executor.submit(imitate_io_job, 1)
#     t_2 = executor.submit(imitate_io_job, 2)

# # Get return value of executed function using 'result()' method of future object
#     print(t_1.result())
#     print(t_2.result())


# print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start}")


# # Multiple threads generator
# with futures.ThreadPoolExecutor() as executor:
#     seconds: list = [5, 4, 3, 2, 1]
#     results: list = [executor.submit(imitate_io_job, sec) for sec in seconds]

#     # Print return values of future objects:

#     # 1. with standard 'for' loop. It prints results in order of job running
#     # for result in results:
#     #     print(result.result())

#     # 2. Using proper 'futures' method that YIELDS! each result AS IT COMPLETES
#     # RETURNS: Future object
#     for result in futures.as_completed(results):
#         print(result.result())


# print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start}")


# Efficient method for creating multiple threads using 'MAP' method

with futures.ThreadPoolExecutor() as executor:
    seconds: list = [5, 4, 3, 2, 1]

    # # RETURNS: Results of function execution (return value / object)
    # results: list = executor.map(imitate_io_job, seconds)

    # # It prints results in order of job running
    # for result in results:
    #     print(result)
