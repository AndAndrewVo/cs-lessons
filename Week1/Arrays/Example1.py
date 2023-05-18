
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(numbers[0])  # Accessing array element
    numbers[2] = 7  # Modifying array element
    for num in numbers:  # Iterating through array
        print(num)
    print("Length:", len(numbers))  # Get length of array
    numbers.remove(4)  # Remove known item
    for num in numbers:
        print(num)
    print("Length:", len(numbers))
    del (numbers[1])  # Delete item in index 1
    for num in numbers:
        print(num)
    print("Length:", len(numbers))

    """
    Expected Output:
    1
    1
    2
    7
    4
    5
    Length: 5
    1
    2
    7
    5
    Length: 5
    1
    7
    5
    Length: 5
    """