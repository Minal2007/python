# Global variable
counter = 0

# Function to increment the counter
def increment():
    global counter  # Use the global variable
    counter += 1
    print(f"Counter value: {counter}")

# Call the function three times
increment()
increment()
increment()
