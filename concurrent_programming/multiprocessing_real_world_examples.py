# import threading
from multiprocessing import Pool
from pathlib import Path
from random import randint, seed
from time import perf_counter

from PIL import Image, ImageFilter

# REAL WORLD EXAMPLE - I/O BOUND TASKS - DOWNLOAD IMAGES ASYNCHRONOUSLY

start: float = perf_counter()


img_names = [
    "photo-1516117172878-fd2c41f4a759.jpg",
    "photo-1532009324734-20a7a5813719.jpg",
    "photo-1524429656589-6633a470097c.jpg",
    "photo-1530224264768-7ff8c1789d79.jpg",
    "photo-1564135624576-c5c88640f235.jpg",
    "photo-1541698444083-023c97d3f4b6.jpg",
    "photo-1522364723953-452d3431c267.jpg",
    "photo-1513938709626-033611b8cc03.jpg",
    "photo-1507143550189-fed454f93097.jpg",
    "photo-1493976040374-85c8e12f0c0e.jpg",
    "photo-1504198453319-5ce911bafcde.jpg",
    "photo-1530122037265-a5f1f91d3b99.jpg",
    "photo-1516972810927-80185027ca84.jpg",
    "photo-1550439062-609e1531270e.jpg",
    "photo-1549692520-acc6669e2f0c.jpg",
]


size = (1200, 1200)


def process_image(img_name, folder_name: str = "raw_images") -> None:
    input_path = Path(folder_name) / img_name
    output_path = Path("processed_images") / img_name
    output_path.parent.mkdir(exist_ok=True)

    try:
        img = Image.open(f"{input_path}")
    except FileNotFoundError:
        print(f"Image {img_name} not found. Skipping...")
        return

    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f"{output_path}")

    print(f"{img_name} was processed...")


# SYNC PROCESSING
# for img_name in img_names:
#     process_image(img_name)

# print(
#     f"Total time of {len(img_names)} image SYNCHRONOUS processing: {perf_counter() - start:.4f} seconds"
# )

# ASYNC PROCESSING

# if __name__ == "__main__":
#     with futures.ProcessPoolExecutor() as executor:
#         executor.map(process_image, img_names)

#     print(
#         f"Total time of {len(img_names)} image ASYNCHRONOUS processing: {perf_counter() - start:.4f} seconds"
#     )


# CPU-BOUND EXAMPLE: PASSING ARGS AND KWARGS TO A FUNCTION USING POOL 'APPLY_ASYNC' METHOD


# Simulate a CPU-bound task that finds prime numbers up to a given upper bound.
def func(a: int, b: int, *, upper_bound: int, job_id: int):
    print(f"Job #{job_id}: {a=}, {b=}, {job_id=}, {upper_bound=}")
    candidates = [False] * 2 + [True] * (upper_bound - 2)
    primes = []

    for i, is_prime in enumerate(candidates):
        if is_prime:
            primes.append(i)
            for n in range(i * i, upper_bound, i):
                candidates[n] = False

    return primes


# Run a pool of processes with a specified job size and pool size
def run_pool(job_size, pool_size):
    jobs = [
        ((i, i + 1), {"job_id": i, "upper_bound": randint(1_000_000, 10_000_000)})
        for i in range(job_size)
    ]
    # create a pool of processes with the specified size
    pool = Pool(processes=pool_size)

    # use apply_async to pass both positional and keyword arguments to the function
    async_results = [
        pool.apply_async(func, args=positionals, kwds=kwargs) for positionals, kwargs in jobs
    ]
    pool.close()

    # wait for async results to come back
    pool.join()

    # get all the results
    results = [result.get() for result in async_results]
    print(results[0])


if __name__ == "__main__":
    start = perf_counter()
    seed(0)

    # run_pool(job_size=100, pool_size=1)
    # run_pool(job_size=100, pool_size=2)
    run_pool(job_size=100, pool_size=4)
    # run_pool(job_size=100, pool_size=8)
    # run_pool(job_size=100, pool_size=20)
    # run_pool(job_size=100, pool_size=50)

    print(f"Elapsed time: {perf_counter() - start:.2f}")
