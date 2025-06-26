from multiprocessing import Pool
from random import randint, seed
from time import perf_counter, sleep

# USE CASE TO DEMONSTRATE MULTIPROCESSING IS NOT EFFICIENT FOR I/O BOUND TASKS


#  Function to simulate a long-running I/O bound job
def long_running_func(job_id, arg1, arg2, sleep_time):
    print(f"running job #{job_id} (sleep={sleep_time})")
    sleep(sleep_time)
    print(f"finished running job #{job_id}")
    return arg1 + arg2


# Function to run a pool of processes with a specified job size and pool size
def run_pool_io(job_size, pool_size):
    """
    Run a pool of processes with the given job size and pool size.
    This function creates a list of jobs, each with a unique ID and random parameters,
    then uses a multiprocessing Pool to execute the jobs concurrently.
    Each job simulates a long-running function that sleeps for a specified time,
    and returns the sum of two random integers.
    The results of all jobs are printed after all processes have completed.

    """

    jobs = [(i, randint(1, 100), randint(1, 100), randint(1, 3)) for i in range(job_size)]

    # Create a multiprocessing Pool with the specified number of processes
    with Pool(processes=pool_size) as pool:
        # use starmap to pass multiple arguments to the long_running_func
        all_results = pool.starmap(long_running_func, jobs)

    # gather all results from all processes
    for result in all_results:
        print(result)


# if __name__ == "__main__":
#     start = perf_counter()
#     seed(0)

#     # INPUT COMMENT HERE

#     """
#     The multiple runs of the pool with different pool sizes below (commented) show that although performance
#     improves with larger pool sizes (parallel runs of the same function/job),
#     results keep improving even beyond the number of CPU cores. This happens because 'sleep()' simulates an I/O-bound task,
#     not a CPU-bound one, allowing interleaving (time-slicing - OS rapidly switches available CPUs between processes)
#     of multiple jobs across the available processes.
#     """

#     # run_pool_io(job_size=50, pool_size=1)
#     # run_pool_io(job_size=50, pool_size=2)
#     # run_pool_io(job_size=50, pool_size=4)
#     # run_pool_io(job_size=50, pool_size=8)

#     run_pool_io(job_size=50, pool_size=50)
#     print(f"Elapsed time: {perf_counter() - start:.2f}")


# USE CASE TO DEMONSTRATE MULTIPROCESSING IS EFFICIENT FOR CPU BOUND TASKS


# Function to simulate a CPU-bound task
def sieve(upper_bound):
    print(f"running sieve: {upper_bound=}")
    candidates = [False] * 2 + [True] * (upper_bound - 2)
    primes = []

    for i, is_prime in enumerate(candidates):
        if is_prime:
            primes.append(i)
            for n in range(i * i, upper_bound, i):
                candidates[n] = False

    return primes


def run_pool_cpu(job_size, pool_size):
    jobs = [randint(1_000_000, 10_000_000) for i in range(job_size)]
    # kick off all the processes
    with Pool(processes=pool_size) as pool:
        all_results = pool.map(sieve, jobs)

    # gather all results from all processes
    print(all_results[0])
    for result in all_results:
        print(f"number of primes found: {len(result)}")


if __name__ == "__main__":
    start = perf_counter()
    seed(0)

    """The multiple runs of the pool with different pool sizes below (commented) show that performance improves with
    larger pool sizes (parallel runs of the same function/job), but results do not improve beyond the number of CPU cores.
    This happens because 'sieve()' simulates a CPU-bound task, which is limited by the number of available CPU cores.
    """

    # run_pool_cpu(job_size=100, pool_size=1)
    # run_pool_cpu(job_size=100, pool_size=2)
    run_pool_cpu(job_size=100, pool_size=4)
    # run_pool_cpu(job_size=100, pool_size=8)
    # run_pool_cpu(job_size=100, pool_size=50)

    print(f"Elapsed time: {perf_counter() - start:.2f}")
