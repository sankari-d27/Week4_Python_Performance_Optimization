
import timeit
import tracemalloc

from original_app import generate_data as original_generate
from original_app import process_data as original_process

from optimized_app import generate_data as optimized_generate
from optimized_app import process_data as optimized_process


def measure_memory(function, data):
    tracemalloc.start()

    function(data)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return peak / 1024


def run_benchmark():

    dataset = original_generate(10000)

    original_time = timeit.timeit(
        lambda: original_process(dataset),
        number=3
    ) / 3

    optimized_time = timeit.timeit(
        lambda: optimized_process(dataset),
        number=3
    ) / 3

    original_memory = measure_memory(original_process, dataset)

    optimized_memory = measure_memory(optimized_process, dataset)

    improvement = (
        ((original_time - optimized_time) / original_time) * 100
        if original_time else 0
    )

    print("\nPERFORMANCE COMPARISON")
    print("----------------------")

    print(f"Original Time: {original_time:.6f} seconds")
    print(f"Optimized Time: {optimized_time:.6f} seconds")

    print(f"Original Memory: {original_memory:.2f} KB")
    print(f"Optimized Memory: {optimized_memory:.2f} KB")

    print(f"Execution Time Improvement: {improvement:.2f}%")

    with open("benchmark_results.txt", "w") as file:
        file.write("PERFORMANCE COMPARISON\n")
        file.write("----------------------\n")
        file.write(f"Original Time: {original_time:.6f} seconds\n")
        file.write(f"Optimized Time: {optimized_time:.6f} seconds\n")
        file.write(f"Original Memory: {original_memory:.2f} KB\n")
        file.write(f"Optimized Memory: {optimized_memory:.2f} KB\n")
        file.write(f"Improvement: {improvement:.2f}%\n")


if __name__ == "__main__":
    run_benchmark()
