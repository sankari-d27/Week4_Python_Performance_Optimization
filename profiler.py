
import cProfile
import pstats
import io

from original_app import generate_data as original_generate
from original_app import process_data as original_process

from optimized_app import generate_data as optimized_generate
from optimized_app import process_data as optimized_process


def profile_application(name, function, data):

    profiler = cProfile.Profile()

    profiler.enable()

    function(data)

    profiler.disable()

    stream = io.StringIO()

    stats = pstats.Stats(profiler, stream=stream)

    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats(20)

    output = stream.getvalue()

    filename = f"{name}_profile.txt"

    with open(filename, "w") as file:
        file.write(output)

    print(f"{name} profiling saved to {filename}")


if __name__ == "__main__":

    dataset = original_generate(10000)

    profile_application(
        "original",
        original_process,
        dataset
    )

    profile_application(
        "optimized",
        optimized_process,
        dataset
    )
