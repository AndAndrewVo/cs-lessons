# Week 1: Arrays, Loops, and Rock Paper Scissors

- Go over arrays
- Go over loops (for/while loop)
- RPS Project

### Arrays
1. Storing multiple values
2. Data manipulation
3. Operations:
   1. Accessing array elements
   2. Modifying elements
   3. Finding length
   4. Examples

#### Array Examples

Array Operations:

- Accessing element
- Modifying element
- Iterating through a array
- Finding length
```python3
numbers = [1, 2, 3, 4, 5]
print(numbers[0])               # Accessing array element
numbers[2] = 7                  # Modifying array element
for num in numbers:             # Iterating through array
    print(num)
print("Length:", len(numbers))  # Get length of array
numbers.remove(4)               # Remove known item
for num in numbers:       
    print(num)
print("Length:", len(numbers))
del(numbers[1])                 # Delete item in index 1
for num in numbers:       
    print(num)
print("Length:", len(numbers))
```

Output:
```text
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
```
---
### Loop Structures
1. Automating repetitive tasks
2. Syntax
3. While  
   1. Specifying conditions
4. For loop
5. Iterating over string, list or range
### Loop Examples

#### Example 1: For Loop
For loop to print out items within `fruits`:
```python3
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

Output:
```text
apple
banana
orange
```

#### Example 2: While Loop

```python3
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

Output:
```text
0
1
2
3
4
```