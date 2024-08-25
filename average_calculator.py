def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    # Taking input from the user
    user_input = input("Enter numbers separated by spaces: ")
    
    # Splitting the input string into a list of integers
    numbers = [int(x) for x in user_input.split()]
    # Calculate the average
    average = calculate_average(numbers)
    print(f"The average is: {average}")
