def generate_fibonacci(n):
    """Generate a Fibonacci sequence up to the nth term."""
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    try:
        upper_limit = int(input("Enter the upper limit to generate Fibonacci sequence: "))
        fibonacci_sequence = generate_fibonacci(upper_limit)
        print("Fibonacci sequence up to", upper_limit, ":", fibonacci_sequence)

        num_to_check = int(input("Enter a number to check if it's prime: "))
        if is_prime(num_to_check):
            print(num_to_check, "is a prime number.")
        else:
            print(num_to_check, "is not a prime number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
