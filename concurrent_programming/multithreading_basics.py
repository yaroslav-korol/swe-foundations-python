import time
from concurrent import futures

import requests

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


# REAL WORLD EXAMPLE

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
