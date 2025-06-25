# import multiprocessing
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

# print(f"Total time of all SYNCHRONOUS jobs run: {time.perf_counter() - start:.4f}")


# ASYNCHRONOUS TASK RUN


# USING MULTIPROCESSING


# MANUAL STEP-BY-STEP APPROACH

# # This guard is required when using multiprocessing on macOS and Windows.
# # These platforms use the 'spawn' method to start new processes, which means
# # the script is re-imported in each child process. Without this check,
# # process creation code would run recursively, causing a RuntimeError.

# if __name__ == "__main__":
#     # Initiate processes
#     process_1 = multiprocessing.Process(target=imitate_io_job, args=(1.5,))
#     process_2 = multiprocessing.Process(target=imitate_io_job, args=(1.5,))

#     # Start process run
#     process_1.start()
#     process_2.start()

#     # Make sure / wait until process finished work
#     process_1.join()
#     process_2.join()

#     print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start:.4f}")


# MULTIPLE PROCESSES GENERATOR

# if __name__ == "__main__":
#     processes: list = [
#         multiprocessing.Process(target=imitate_io_job, args=(1.5,)) for _ in range(10)
#     ]

#     # Start processes run
#     for process in processes:
#         process.start()

#     # Wait until all processes finished work
#     for process in processes:
#         process.join()

#     print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start:.4f}")


# USING CONCURRENT FUTURES


# MANUAL STEP-BY-STEP APPROACH

# if __name__ == "__main__":
#     # Create a future objects with 'executor' context manager
#     with futures.ProcessPoolExecutor() as executor:
#         # Submit tasks to the executor
#         future_1 = executor.submit(imitate_io_job, 1.5)
#         future_2 = executor.submit(imitate_io_job, 1.5)

#         # Wait for the futures to complete and get results
#         result_1 = future_1.result()
#         result_2 = future_2.result()

#         print(result_1)
#         print(result_2)

#     print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start:.4f}")


# MULTIPLE PROCESSES GENERATOR WITH CONCURRENT FUTURES

# if __name__ == "__main__":
#     # Create a future objects with 'executor' context manager
#     with futures.ProcessPoolExecutor() as executor:
#         seconds: list = [5, 4, 3, 2, 1]
#         results: list = [executor.submit(imitate_io_job, sec) for sec in seconds]

#         # Print return values of future objects:

#         # 1. with standard 'for' loop. It prints results in order of job running
#         # for future in results:
#         #     print(future.result())

#         # 2. Using proper 'futures' method that YIELDS! each result AS IT COMPLETES
#         # RETURNS: Future object
#         for result in futures.as_completed(results):
#             print(result.result())

#     print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start:.4f}")


# EFFICIENT METHOD FOR CREATING MULTIPLE PROCESSES USING 'MAP' METHOD


if __name__ == "__main__":
    with futures.ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]

        # RETURNS: Results of function execution (return value / object)
        results = executor.map(imitate_io_job, seconds)

        # Prints the results in order of job running
        for result in results:
            print(result)

    print(f"Total time of all ASYNCHRONOUS jobs run: {time.perf_counter() - start:.4f}")
