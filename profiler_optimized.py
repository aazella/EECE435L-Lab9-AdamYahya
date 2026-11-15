import time

def slow_function():
    time.sleep(2)  
    n = 10000
    return (n - 1) * n * (2 * n - 1) // 6  


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
    main()
