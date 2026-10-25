# Laboratory Practice n. 7 - Python (Exercises 1-8)

Turin Polytechnic University in Tashkent - Course of Computer Science

Topic: **sorting algorithms (Bubble sort, Insertion sort, Merge sort)**.

---

## First-time Git setup

Before you commit your code, configure your Git username and email.
Run these commands once in your terminal:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.student.email@example.com"
```

If you do not run these commands, Git can block your commit with an author identity error.

---

## How to start

1. Open this repository in GitHub Codespaces: click **Code -> Codespaces -> Create codespace on main**.
2. Wait for the environment to load. Python installs automatically.
3. Open the file for the exercise, for example `ex1.py`.
4. Write your code below the comment `# Write your solution below.`
5. Click the **Run Python File** button (top-right of the editor) or press the play button.

You can also run any file in the terminal:

```bash
python ex1.py
```

Do not rename the files. Some files already contain data. Use this data in your solution.

---

## How to submit

Run these commands in the terminal:

```bash
git add .
git commit -m "Solve lab 7"
git push
```

We grade only the code on GitHub.

---

## Useful reminders

```python
# Swap two items in a list
arr[i], arr[j] = arr[j], arr[i]

# Copy a list before modifying it
my_list = numbers.copy()

# Find the middle index of a list
mid = len(arr) // 2

# Slice a list into left and right halves
left_half = arr[:mid]
right_half = arr[mid:]

# Combine two lists
merged.extend(remaining_items)  # or: merged += remaining_items

# Compare strings alphabetically
"Aziz" < "Malika"               # evaluates to True

# Access dictionary fields
student["exam_score"]
product["price"]

# Measure execution time in seconds
import time
start = time.perf_counter()
# run your function here
elapsed = time.perf_counter() - start

# Import datasets from dataset.py
from dataset import small_numbers, students, products
```

---

## Exercise 1 - Bubble sort step-by-step

Bubble Sort is one of the simplest sorting algorithms. It steps through a list, compares adjacent items, and swaps them if they are in the wrong order. After the first complete pass, the largest item rises ("bubbles up") to the end of the list.

The data is in `ex1.py`:

```python
numbers = [64, 34, 25, 12, 22, 11, 90]
```

1. Sort a copy of `numbers` in ascending order using Bubble Sort.
2. Print the list after each complete pass (Pass 1 through Pass 6).
3. Count how many total comparisons and swaps your code makes.
4. Print the final sorted list and the total counts.

Hints:
- Use two nested loops: an outer loop for the passes, and an inner loop for adjacent comparisons.
- In each pass `i`, compare `arr[j]` with `arr[j + 1]`. If `arr[j] > arr[j + 1]`, swap them.
- Swap elements cleanly using Python tuple assignment: `arr[j], arr[j + 1] = arr[j + 1], arr[j]`.
- Notice that after pass `i`, the largest `i` items are already in their final places. The inner loop only needs to check up to `len(arr) - 1 - i`.

Output:

```text
Initial list: [64, 34, 25, 12, 22, 11, 90]

Pass 1: [34, 25, 12, 22, 11, 64, 90]
Pass 2: [25, 12, 22, 11, 34, 64, 90]
Pass 3: [12, 22, 11, 25, 34, 64, 90]
Pass 4: [12, 11, 22, 25, 34, 64, 90]
Pass 5: [11, 12, 22, 25, 34, 64, 90]
Pass 6: [11, 12, 22, 25, 34, 64, 90]

Sorted list: [11, 12, 22, 25, 34, 64, 90]
Total comparisons: 21
Total swaps: 14
```

---

## Exercise 2 - Optimized bubble sort (early exit)

A standard Bubble Sort always executes all $n - 1$ passes, even if the list becomes sorted after just one or two passes. We can optimize it by tracking whether any swap occurred during a pass. If no items were swapped, the list is already sorted, and we can stop immediately!

The data is in `ex2.py`:

```python
nearly_sorted = [10, 20, 25, 30, 50, 40, 60, 70]
already_sorted = [5, 15, 25, 35, 45, 55]
```

1. Implement an optimized Bubble Sort that uses a boolean variable `swapped`.
2. Test your algorithm on `nearly_sorted`. Print the list after each pass, and print a message when an early stop occurs.
3. Test your algorithm on `already_sorted`. Show that it stops after only 1 pass.
4. For each test, print how many passes were executed compared to how many passes a standard Bubble Sort would need.

Hints:
- Set `swapped = False` before each pass starts.
- When a swap happens, change `swapped = True`.
- At the end of each pass, check `if not swapped:`. If `swapped` is `False`, break out of the outer loop.

Output:

```text
--- Testing nearly_sorted ---
List: [10, 20, 25, 30, 50, 40, 60, 70]
Pass 1: [10, 20, 25, 30, 40, 50, 60, 70]
Pass 2: [10, 20, 25, 30, 40, 50, 60, 70] (no swaps, stopping early!)
Optimized passes: 2 (Standard would take 7 passes)
Sorted list: [10, 20, 25, 30, 40, 50, 60, 70]

--- Testing already_sorted ---
List: [5, 15, 25, 35, 45, 55]
Pass 1: [5, 15, 25, 35, 45, 55] (no swaps, stopping early!)
Optimized passes: 1 (Standard would take 5 passes)
Sorted list: [5, 15, 25, 35, 45, 55]
```

---

## Exercise 3 - Insertion sort step-by-step

Insertion Sort builds a sorted list one item at a time. It works like sorting playing cards in your hand: you divide your list into a sorted section on the left and an unsorted section on the right. For each unsorted item, you pick it up (`key`), shift all larger items one position to the right, and insert the `key` into its correct spot.

The data is in `ex3.py`:

```python
numbers = [29, 10, 14, 37, 13]
```

1. Sort a copy of `numbers` in ascending order using Insertion Sort.
2. Start your outer loop from index `1` up to the end of the list.
3. In each step:
   - Save the current value into a variable named `key`.
   - Use a `while` loop to shift all elements greater than `key` one position to the right.
   - Insert `key` at the correct index.
4. Print the list and the value of `key` after each insertion step.
5. Count and print the total number of shifts made.

Hints:
- To shift elements, set `j = i - 1`. While `j >= 0` and `arr[j] > key`: copy `arr[j]` to `arr[j + 1]`, increase your shift count by 1, and decrement `j -= 1`.
- Place `key` with `arr[j + 1] = key`.
- An element of 1 item (at index 0) is already considered sorted, which is why the outer loop begins at index 1.

Output:

```text
Initial list: [29, 10, 14, 37, 13]

Step 1 (insert 10): [10, 29, 14, 37, 13]
Step 2 (insert 14): [10, 14, 29, 37, 13]
Step 3 (insert 37): [10, 14, 29, 37, 13]
Step 4 (insert 13): [10, 13, 14, 29, 37]

Sorted list: [10, 13, 14, 29, 37]
Total shifts: 5
```

---

## Exercise 4 - Insertion sort with strings

Sorting algorithms work on text and words just like they work on numbers! In Python, strings are compared alphabetically. Insertion Sort is especially useful when you need to maintain an already sorted list as new elements arrive.

The data is in `ex4.py`:

```python
names = ["Sardor", "Malika", "Aziz", "Dilnoza", "Jasur", "Kamola"]
new_student = "Bekzod"
```

1. Sort `names` alphabetically in **ascending order** (A to Z) using Insertion Sort. Print the sorted list.
2. Sort a copy of `names` in **descending order** (Z to A) using Insertion Sort. Print the descending list.
3. Imagine a new student joins the class: add `new_student = "Bekzod"` to the ascending sorted roster. Insert `"Bekzod"` into its correct alphabetical position in **one single insertion pass**, without re-sorting the whole list. Print the updated roster.

Hints:
- In Python, string comparisons like `"Aziz" < "Dilnoza"` evaluate to `True`.
- For descending order, change the comparison inside the `while` loop: shift elements when `arr[j] < key`.
- For step 3, append `"Bekzod"` to the end of the list with `.append()`, then run your `while` shift loop once starting from the last index (`len(arr) - 1`).

Output:

```text
Initial roster: ['Sardor', 'Malika', 'Aziz', 'Dilnoza', 'Jasur', 'Kamola']

Sorted roster (A-Z):
['Aziz', 'Dilnoza', 'Jasur', 'Kamola', 'Malika', 'Sardor']

Sorted roster (Z-A):
['Sardor', 'Malika', 'Kamola', 'Jasur', 'Dilnoza', 'Aziz']

Adding new student: 'Bekzod'
Updated roster (A-Z):
['Aziz', 'Bekzod', 'Dilnoza', 'Jasur', 'Kamola', 'Malika', 'Sardor']
```

---

## Exercise 5 - Merge sort: The merge step

Merge Sort is a **divide-and-conquer** algorithm. Before writing the full recursive algorithm, master its most important building block: the `merge(left, right)` function.

The function takes two lists that are **already sorted** and combines them into one sorted list.

The data is in `ex5.py`:

```python
list_a = [3, 9, 15, 27]
list_b = [2, 8, 18, 20, 25]
```

1. Write a function `merge(left, right)`:
   - Create an empty list `merged = []`.
   - Maintain two pointers: `i = 0` for `left`, and `j = 0` for `right`.
   - While `i < len(left)` and `j < len(right)`: compare `left[i]` and `right[j]`. Append the smaller item to `merged` and advance that pointer by 1.
   - After the loop, append any remaining items from `left` and `right`.
   - Return `merged`.
2. Test `merge(list_a, list_b)` and print the merged result.
3. Test edge case behavior by merging an empty list with `[1, 2, 3]`.

Hints:
- Use `merged.extend(left[i:])` to append all leftover elements from `left` when `right` is exhausted.
- Do not use Python's built-in `sorted()` or `.sort()` — write the pointer comparison logic manually.

Output:

```text
List A: [3, 9, 15, 27]
List B: [2, 8, 18, 20, 25]

Merged result:
[2, 3, 8, 9, 15, 18, 20, 25, 27]

Test empty list merge:
Merged with empty: [1, 2, 3]
```

---

## Exercise 6 - Full merge sort implementation

Now complete the full Merge Sort algorithm using recursion.

Merge Sort follows three steps:
1. **Divide**: Find the midpoint `mid = len(arr) // 2`. Split the list into `left = arr[:mid]` and `right = arr[mid:]`.
2. **Conquer**: Recursively call `merge_sort()` on both halves until each sublist has 1 or 0 elements (**base case**).
3. **Combine**: Call `merge(sorted_left, sorted_right)` to combine the sorted halves.

The data is in `ex6.py`:

```python
numbers = [38, 27, 43, 3, 9, 82, 10]
```

1. Write `merge_sort(arr)` using recursion.
2. Define the base case: `if len(arr) <= 1: return arr`.
3. Add print statements to trace the divide and merge steps so you can observe the recursion in action.
4. Sort `numbers` and print the final sorted list.

Hints:
- Integer division `//` gives an integer midpoint index.
- Slicing `arr[:mid]` takes elements from index 0 to `mid - 1`. Slicing `arr[mid:]` takes elements from `mid` to the end.
- Unlike Bubble Sort and Insertion Sort which sort lists in place, Merge Sort produces and returns a new sorted list.

Output:

```text
Initial list: [38, 27, 43, 3, 9, 82, 10]

Split: [38, 27, 43] and [3, 9, 82, 10]
  Split: [38] and [27, 43]
    Split: [27] and [43]
    Merged: [27, 43]
  Merged: [27, 38, 43]
  Split: [3, 9] and [82, 10]
    Split: [3] and [9]
    Merged: [3, 9]
    Split: [82] and [10]
    Merged: [10, 82]
  Merged: [3, 9, 10, 82]
Merged: [3, 9, 10, 27, 38, 43, 82]

Final sorted list: [3, 9, 10, 27, 38, 43, 82]
```

---

## Exercise 7 - Comparing sorting performance

Why do we study different sorting algorithms? On small lists, the difference in execution speed is unnoticeable. But as data grows, the choice of algorithm becomes critical!

In this exercise, you compare **Bubble Sort**, **Insertion Sort**, and **Merge Sort** across different input sizes and orderings.

Import the datasets in `ex7.py`:

```python
from dataset import small_benchmark_list, large_sorted_numbers, large_unsorted_numbers
```

1. **Test 1 - Comparisons on small data**: Count how many element comparisons each algorithm makes when sorting `small_benchmark_list` (20 elements).
2. **Test 2 - Runtime on large unsorted data**: Measure the execution time in seconds (`time.perf_counter()`) for each algorithm on `large_unsorted_numbers` (2,000 elements).
3. **Test 3 - Best-case behavior**: Measure execution time on `large_sorted_numbers` (2,000 elements) for optimized Bubble Sort, Insertion Sort, and Merge Sort.
4. Print the comparison results and a brief 3-point conclusion.

Hints:
- Always make a copy of your test list before sorting: `test_data = data.copy()`. If you do not copy it, the first algorithm will sort it in place, leaving already sorted data for the next algorithm!
- Record elapsed time:
  ```python
  start = time.perf_counter()
  my_sort(test_data)
  elapsed = time.perf_counter() - start
  ```
- Bubble Sort and Insertion Sort have quadratic complexity ($O(n^2)$) on unsorted data, while Merge Sort has linearithmic complexity ($O(n \log n)$).

Output:

```text
--- Test 1: Small List (20 elements) ---
Bubble Sort:    187 comparisons
Insertion Sort: 114 comparisons
Merge Sort:     65 comparisons

--- Test 2: Large Unsorted List (2,000 elements) ---
Bubble Sort:    ~0.250 seconds
Insertion Sort: ~0.115 seconds
Merge Sort:     ~0.005 seconds

--- Test 3: Already Sorted List (2,000 elements) ---
Optimized Bubble: ~0.0002 seconds
Insertion Sort:   ~0.0003 seconds
Merge Sort:       ~0.0030 seconds

Conclusion:
1. Merge Sort is significantly faster on large unsorted data (O(n log n) vs O(n^2)).
2. Insertion Sort and Optimized Bubble Sort are extremely fast on already-sorted data (O(n)).
3. Bubble Sort is simple to understand, but inefficient for large real-world collections.
```

---

## Exercise 8 - Sorting real-world records

In practical software engineering, you rarely sort plain numbers. Most data consists of dictionaries, records, or objects. You must be able to sort by different fields and in different directions (ascending vs. descending).

Import the datasets in `ex8.py`:

```python
from dataset import students, products
```

Sample student record:
```python
{"id": "U24101", "name": "Malika", "group": "CS-01", "gpa": 3.85, "exam_score": 92}
```

Sample product record:
```python
{"id": 1001, "name": "Mouse #1001", "category": "Electronics", "price": 10.0}
```

1. **Rank students by exam score**:
   Sort `students` in **descending order** (highest score first) using **Insertion Sort** based on `student["exam_score"]`. Print the top 3 students.
2. **Sort students alphabetically**:
   Sort `students` in **ascending order** by `student["name"]` using **Bubble Sort**. Print all student names and their groups.
3. **Find the cheapest products**:
   Sort `products` in **ascending order** by `product["price"]` using **Merge Sort**. Print the 3 cheapest products.
4. **Stable sort check**:
   In `students`, both Kamola and Madina have an exam score of `88`. Notice that their original relative order was preserved after sorting.

Hints:
- When comparing records, compare the specific dictionary key: `arr[j]["exam_score"] < key["exam_score"]`.
- Swap or shift the **entire dictionary**, not just the score!
- For stable sorting with Insertion Sort, use `<` (strictly less than) rather than `<=` so items with equal scores stay in their original relative positions.

Output:

```text
--- Top 3 Students by Exam Score ---
1. Nigora (Score: 98, GPA: 3.95)
2. Dilnoza (Score: 95, GPA: 3.9)
3. Malika (Score: 92, GPA: 3.85)

--- Students Sorted Alphabetically ---
1. Aziz (CS-02)
2. Bekzod (CS-03)
3. Dilnoza (CS-01)
4. Jasur (CS-02)
5. Javohir (CS-01)
6. Kamola (CS-01)
7. Madina (CS-03)
8. Malika (CS-01)
9. Nigora (CS-02)
10. Sardor (CS-03)

--- Top 3 Cheapest Products ---
1. Mouse #1001 - $10.0
2. Headphones #1091 - $10.0
3. Clean Code #1017 - $12.99
```
