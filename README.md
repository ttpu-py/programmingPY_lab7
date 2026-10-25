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

## Lab Rules: Focus on Fundamentals

> [!IMPORTANT]
> **No Built-in Shortcuts Allowed!**
>
> Python includes high-level convenience tools like `.sort()` and `sorted()`.
> In this lab, you are **not** allowed to use:
> - `list.sort()` or `sorted(...)`
> - `min(...)` or `max(...)`
> - `list.index(...)`
> - `reversed(...)`
> - External sorting libraries (`heapq`, `bisect`, etc.)
>
> **The Goal**: As a computer scientist, you must understand what the computer does step-by-step: indices, comparisons, pointer movements, memory shifts, and recursion. You must write every loop and comparison manually.

---

## Useful reminders

```python
# 1. Swapping two items in a list (Python tuple swap)
arr[i], arr[j] = arr[j], arr[i]

# 2. Copying a list (DO NOT write b = a; that only creates an alias!)
arr_copy = original_list.copy()

# 3. Integer division for the midpoint
mid = len(arr) // 2

# 4. Slicing a list in half
left_half = arr[:mid]       # from index 0 to mid - 1
right_half = arr[mid:]      # from index mid to the end

# 5. Short-circuit evaluation in while loops
# ALWAYS check 'j >= 0' first!
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
    j -= 1

# 6. Comparing strings alphabetically
"Aziz" < "Malika"           # True (A comes before M)

# 7. Accessing dictionary fields
student["exam_score"]
product["price"]

# 8. Measuring time in seconds
import time
start = time.perf_counter()
# run your function here
elapsed = time.perf_counter() - start

# 9. Importing datasets from dataset.py
from dataset import small_numbers, students, products
```

---

## Exercise 1 - Bubble sort step-by-step

Bubble Sort is the most intuitive sorting algorithm. It makes multiple passes through a list. In each pass, it compares adjacent elements (`arr[j]` and `arr[j + 1]`). If the left item is greater than the right item, it swaps them.

After the first pass, the largest number moves to the very end of the list — just like a bubble rising to the surface.

The data is in `ex1.py`:

```python
numbers = [64, 34, 25, 12, 22, 11, 90]
```

1. Create a copy of `numbers` so you do not modify the original list directly: `arr = numbers.copy()`.
2. Write Bubble Sort using two nested loops:
   - Outer loop `i`: controls the number of passes (`0` to `len(arr) - 2`).
   - Inner loop `j`: checks adjacent pairs (`0` to `len(arr) - 2 - i`).
3. Inside the inner loop:
   - Increase a `comparisons` counter by 1.
   - If `arr[j] > arr[j + 1]`, swap them and increase a `swaps` counter by 1.
4. After each complete outer pass, print the current state of the list.
5. After all passes finish, print the final sorted list, the total comparisons, and total swaps.

Hints:
- **Avoiding IndexError**: If a list has length 7, the highest index is 6. If `j` reached 6, checking `arr[j + 1]` (index 7) would crash with an `IndexError`. That is why the inner loop range stops at `len(arr) - 1 - i`.
- **Why `- i`?**: After pass 0, the 1 largest item is placed. After pass 1, the 2 largest items are placed. You do not need to re-check the end of the list!
- Remember: **Do not use `.sort()` or `sorted()`**.

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

Notice in Exercise 1 that after Pass 5, the list was already sorted: `[11, 12, 22, 25, 34, 64, 90]`. Yet Pass 6 still ran and made comparisons without swapping anything!

Standard Bubble Sort is slow because it always performs all $n - 1$ passes. We can optimize it with a boolean flag:
If a full pass completes with **zero swaps**, the list is already sorted! We can stop immediately with `break`.

The data is in `ex2.py`:

```python
nearly_sorted = [10, 20, 25, 30, 50, 40, 60, 70]
already_sorted = [5, 15, 25, 35, 45, 55]
```

1. Implement an optimized Bubble Sort function or loop structure using a boolean flag `swapped`.
2. Test on `nearly_sorted`:
   - Set `swapped = False` before starting each pass.
   - If any swap occurs during the pass, set `swapped = True`.
   - At the end of the pass, if `swapped` is still `False`, print `(no swaps, stopping early!)` and `break`.
3. Test on `already_sorted`: verify that your code executes only 1 pass and stops.
4. For both tests, print how many passes your code ran compared to a standard unoptimized sort ($n - 1$ passes).

Hints:
- Place `swapped = False` right inside the outer loop, before the inner loop begins.
- If no elements are swapped throughout the entire inner loop, `if not swapped:` triggers the `break`.

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

Insertion Sort works like sorting cards in your hands. You maintain two portions in the list:
- A **sorted portion** on the left.
- An **unsorted portion** on the right.

At each step, you pick the next unsorted card (the `key`), shift all elements in the sorted portion that are larger than `key` one position to the right, and insert `key` into the vacated space.

The data is in `ex3.py`:

```python
numbers = [29, 10, 14, 37, 13]
```

1. Start your outer loop from index `1` up to `len(numbers) - 1` (an initial list of 1 element at index 0 is already sorted by definition!).
2. In each iteration `i`:
   - Store the current item in a temporary variable: `key = arr[i]`.
   - Set pointer `j = i - 1`.
   - Use a `while` loop to shift elements to the right as long as `j >= 0` and `arr[j] > key`.
   - Shift an element: `arr[j + 1] = arr[j]`. Increment a `shifts` counter. Decrement `j -= 1`.
   - Once the while loop stops, insert the key: `arr[j + 1] = key`.
3. Print the list and the inserted key after each step.
4. Print the final sorted list and the total number of shifts.

Hints:
- **Crucial Python Trait (Short-circuit Evaluation)**:
  Always write `while j >= 0 and arr[j] > key:` — NEVER `while arr[j] > key and j >= 0:`.
  If `j` reaches `-1`, Python checks `j >= 0` first, evaluates to `False`, and stops. If you checked `arr[j]` first, Python would access `arr[-1]` (the last element of the list!) and create bugs.

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

Sorting algorithms are general: they work on text just as well as numbers! Python compares strings in alphabetical (lexicographical) order (`"Aziz" < "Malika"` is `True`).

Insertion Sort has a major real-world superpower: **online sorting**. If you already have a sorted list and one new item arrives, you can insert it into its exact position in $O(n)$ time without re-sorting the whole list!

The data is in `ex4.py`:

```python
names = ["Sardor", "Malika", "Aziz", "Dilnoza", "Jasur", "Kamola"]
new_student = "Bekzod"
```

1. Sort `names` alphabetically in **ascending order** (A to Z) using Insertion Sort. Print the sorted roster.
2. Sort a fresh copy of `names` in **descending order** (Z to A) using Insertion Sort. Print the descending roster.
3. A new student `"Bekzod"` joins the class:
   - Add `"Bekzod"` to the end of your ascending sorted roster: `names.append(new_student)`.
   - Run a single insertion step starting from the last element (`key = names[-1]`, `j = len(names) - 2`) to shift items and place `"Bekzod"` where it belongs.
   - Print the updated roster.

Hints:
- For descending order, change the shift condition from `arr[j] > key` to `arr[j] < key`.
- For step 3: **Do not call `.sort()` or sort the whole list from scratch!** Use the while-loop shift logic once on the last item.

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

Merge Sort is a **divide-and-conquer** algorithm. It works in two phases:
1. Divide the list into smaller halves until each sublist has 1 item.
2. Merge the sorted sublists back together.

Before touching recursion, master the most crucial part: the **two-pointer merge function**. This function takes two lists that are **already sorted** and combines them into one sorted list.

The data is in `ex5.py`:

```python
list_a = [3, 9, 15, 27]
list_b = [2, 8, 18, 20, 25]
```

1. Write a function `merge(left, right)`:
   - Create an empty list: `merged = []`.
   - Use two pointer indices: `i = 0` (for `left`) and `j = 0` (for `right`).
   - While `i < len(left)` and `j < len(right)`:
     - Compare `left[i]` and `right[j]`.
     - Append the smaller item to `merged` and advance that pointer by 1 (`i += 1` or `j += 1`).
   - After the loop finishes, one list still has leftover elements. Append all remaining elements to `merged`:
     ```python
     while i < len(left):
         merged.append(left[i])
         i += 1
     while j < len(right):
         merged.append(right[j])
         j += 1
     ```
   - Return `merged`.
2. Test `merge(list_a, list_b)` and print the result.
3. Test edge-case behavior by merging an empty list `[]` with `[1, 2, 3]`.

Hints:
- Notice how the two pointers move independently like two fingers walking through two decks of cards.
- You can also append leftovers with `merged.extend(left[i:])` and `merged.extend(right[j:])`.

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

Now complete the recursive Merge Sort algorithm.

Recursion means a function calls itself to solve smaller pieces of the same problem. Every recursive function needs two things:
1. **Base Case**: A condition to stop recursion. A list with 0 or 1 element is already sorted.
2. **Recursive Step**: Split the list in half, recursively sort each half, and merge them with `merge()`.

The data is in `ex6.py`:

```python
numbers = [38, 27, 43, 3, 9, 82, 10]
```

1. Write `merge_sort(arr)`:
   - Base case: `if len(arr) <= 1: return arr`.
   - Find the midpoint: `mid = len(arr) // 2`.
   - Divide: `left = arr[:mid]` and `right = arr[mid:]`.
   - Conquer: `sorted_left = merge_sort(left)` and `sorted_right = merge_sort(right)`.
   - Combine: `return merge(sorted_left, sorted_right)` (use your function from Exercise 5).
2. Add print statements before dividing and after merging to trace how the list splits and recombines.
3. Call `merge_sort(numbers)` and print the final sorted list.

Hints:
- Integer division `//` ensures you get a valid whole number index for `mid`.
- Unlike Bubble Sort and Insertion Sort (which modify the list in place), Merge Sort creates and returns new sorted lists.

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

Why learn multiple sorting algorithms?
On 10 elements, any algorithm finishes in a fraction of a millisecond. But in industry, programs process millions of records. The difference between an $O(n^2)$ algorithm and an $O(n \log n)$ algorithm is the difference between waiting **10 hours** and waiting **3 seconds**!

Import the datasets in `ex7.py`:

```python
from dataset import small_benchmark_list, large_sorted_numbers, large_unsorted_numbers
```

1. **Test 1 - Counting comparisons on small data (20 elements)**:
   Sort `small_benchmark_list` (20 elements). Count how many comparisons Bubble Sort makes vs. Insertion Sort vs. Merge Sort.
2. **Test 2 - Measuring time on large unsorted data (2,000 elements)**:
   Measure the elapsed time in seconds (`time.perf_counter()`) for Bubble Sort, Insertion Sort, and Merge Sort on `large_unsorted_numbers`.
3. **Test 3 - Best-case performance on sorted data (2,000 elements)**:
   Measure the elapsed time on `large_sorted_numbers` for optimized Bubble Sort, Insertion Sort, and Merge Sort.
4. Print the comparison table and a short conclusion.

Hints:
- **Always copy the list**:
  `test_list = large_unsorted_numbers.copy()`. If you do not copy, the first algorithm sorts the list, and subsequent algorithms will mistakenly test on already sorted data!
- For counting comparisons in Merge Sort: count comparisons inside the `while i < len(left) and j < len(right):` loop of `merge()`.

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
1. Merge Sort is roughly 50x faster on large unsorted data (O(n log n) vs O(n^2)).
2. Insertion Sort and Optimized Bubble Sort beat Merge Sort on already-sorted data (O(n)).
3. Never use unoptimized Bubble Sort on large collections.
```

---

## Exercise 8 - Sorting real-world records

In practical software, data is stored in dictionaries or objects. You frequently need to sort records by specific keys (e.g., student score, GPA, or product price).

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
   Sort a copy of `students` in **descending order** (highest score first) using **Insertion Sort** based on `student["exam_score"]`. Print the top 3 students.
2. **Sort students alphabetically**:
   Sort a copy of `students` in **ascending order** by `student["name"]` using **Bubble Sort**. Print all 10 students.
3. **Find cheapest products**:
   Sort a copy of `products` in **ascending order** by `product["price"]` using **Merge Sort**. Print the 3 cheapest products.
4. **Observe stability**:
   Both Kamola and Madina have an exam score of `88`. In the original list, Kamola appears before Madina. Verify that Kamola still appears before Madina in the ranked output. (A sort that preserves the relative order of equal items is called a **stable sort**).

Hints:
- **Major Pitfall**: Compare the dictionary field (`arr[j]["exam_score"] < key["exam_score"]`), but swap or shift the **entire dictionary** (`arr[j + 1] = arr[j]`), not just the score! If you swap only the score, you corrupt student records!
- To sort in descending order with Insertion Sort, shift elements when `arr[j]["exam_score"] < key["exam_score"]`.
- To preserve stability, use strictly less than `<` instead of `<=`.

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
