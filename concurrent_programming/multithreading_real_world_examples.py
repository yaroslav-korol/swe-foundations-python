import math
import threading
from concurrent import futures
from time import perf_counter

import requests

# REAL WORLD EXAMPLE - I/O BOUND TASKS - DOWNLOAD IMAGES ASYNCHRONOUSLY

img_urls: list[str] = [
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
    "https://images.unsplash.com/photo-1532009324734-20a7a5813719",
    "https://images.unsplash.com/photo-1524429656589-6633a470097c",
    "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79",
    "https://images.unsplash.com/photo-1564135624576-c5c88640f235",
    "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6",
    "https://images.unsplash.com/photo-1522364723953-452d3431c267",
    "https://images.unsplash.com/photo-1513938709626-033611b8cc03",
    "https://images.unsplash.com/photo-1507143550189-fed454f93097",
    "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e",
    "https://images.unsplash.com/photo-1504198453319-5ce911bafcde",
    "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99",
    "https://images.unsplash.com/photo-1516972810927-80185027ca84",
    "https://images.unsplash.com/photo-1550439062-609e1531270e",
    "https://images.unsplash.com/photo-1549692520-acc6669e2f0c",
]


def download_image(image_url: str) -> int:
    response_binary = requests.get(url=image_url).content
    image_name: str = f"{image_url.split('/')[3]}.jpg"

    with open(image_name, "wb") as downloaded_image:
        downloaded_image.write(response_binary)
        print(f"{image_name} downloaded successfully")

    return 0


# ASYNC DOWNLOAD
with futures.ThreadPoolExecutor() as executor:
    downloaded_images: list[str] = executor.map(download_image, img_urls)

    for result in downloaded_images:
        print(result)

# SYNC DOWNLOAD
# for url in img_urls:
#     download_image(image_url=url)

print(
    f"Total time of {len(img_urls)} ASYNCHRONOUS images download: {time.perf_counter() - start} seconds"
)


# REAL WORLD EXAMPLE - CPU BOUND TASKS - MULTI-THREADING Riemann Sums


NUM_INTERVALS = 10_000_000
NUM_THREADS = 10_000
results = []


def func(x):
    # semi-circle, radius 1, centered at (0, 0)
    # integral from -1 to 1 of this function should gives us
    # the area of this semi-circle: pi / 2
    return math.sqrt(1 - x * x)


# SINGLE THREAD SOLUTION


def riemann_sum(func, delta, a, i_start, i_end):
    # calculates the right Riemann sums
    area = 0
    for i in range(i_start, i_end):
        x = a + delta * i
        area += func(x) * delta
    return area


# if __name__ == "__main__":
#     start = perf_counter()
#     a = -1
#     b = 1
#     delta = (b - a) / NUM_INTERVALS
#     area = riemann_sum(func, delta, a, 0, NUM_INTERVALS)
#     end = perf_counter()
#     print(f"Area: {area:.10f}, pi/2={math.pi / 2:.10f}")
#     print(f"Elapsed: {end - start:.4f} seconds")


# MULTI-THREAD SOLUTION


def riemann_sum_multithreaded(func, delta, a, i_start, i_end):
    # calculates the right Riemann sums
    area = 0
    for i in range(i_start, i_end):
        x = a + delta * i
        area += func(x) * delta
    results.append(area)


def split(num_intervals, n):
    k, m = divmod(num_intervals, n)
    return [(i * k + min(i, m), (i + 1) * k + min(i + 1, m)) for i in range(n)]


if __name__ == "__main__":
    start = perf_counter()
    a = -1
    b = 1
    delta = (b - a) / NUM_INTERVALS

    # split the intervals into NUM_THREADS
    chunks = split(NUM_INTERVALS, NUM_THREADS)

    # Create the threads
    threads = []
    for i_start, i_end in chunks:
        threads.append(
            threading.Thread(
                target=riemann_sum_multithreaded, args=(func, delta, a, i_start, i_end)
            )
        )

    # Start and join the threads
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # all threads done processing - add all results up for final answer
    area = sum(results)

    end = perf_counter()
    print(f"Area: {area:.10f}, pi/2={math.pi / 2:.10f}")
    print(f"Elapsed: {end - start:.4f} seconds")
