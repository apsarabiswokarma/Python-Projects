def min_max(numbers):
    # Initialize the minimum and maximum values to the first element in the list
    min_val = numbers[0]
    max_val = numbers[0]

    # Iterate through the rest of the list
    for i in range(1, len(numbers)):
        # Update the minimum and maximum values if necessary
        min_val = min(min_val, numbers[i])
        max_val = max(max_val, numbers[i])

    return (min_val, max_val)


# Test the function
print(min_max([7, 9, 2, 1, 5]))
