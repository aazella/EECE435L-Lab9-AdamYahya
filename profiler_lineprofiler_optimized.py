import time

from line_profiler import LineProfiler


def profile_main():
    profiler = LineProfiler()
    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(memory_intensive_function)
    profiler.runcall(main)
    profiler.print_stats()


def slow_function():
    time.sleep(2) 
    n = 10000
    return (n - 1) * n * (2 * n - 1) // 6  # replace the  loop


def optimized_fast_function():
    n = 100
    return (n - 1) * n * (2 * n - 1) // 6  


def memory_intensive_function():
    n = 10000000
    return (n - 1) * n * (2 * n - 1) // 6  


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    profile_main()
