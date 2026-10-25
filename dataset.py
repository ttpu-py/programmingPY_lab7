"""
Laboratory Practice n. 7 - Dataset Module
Turin Polytechnic University in Tashkent - Course of Computer Science

Topic: Sorting Algorithms (Bubble Sort, Insertion Sort, Merge Sort).

This file provides small and large datasets for your exercises.
You can import any variable into your exercise files.

Example:
    from dataset import small_numbers, large_unsorted_numbers, students
"""

import random

# Seed for reproducible results across all students
_rng = random.Random(42)

# --- Small datasets (for tracing and step-by-step exercises) ---

# Exercise 1: Classic list for tracing Bubble Sort
small_numbers = [64, 34, 25, 12, 22, 11, 90]

# Exercise 2: Nearly sorted and already sorted lists for early-exit Bubble Sort
nearly_sorted = [10, 20, 25, 30, 50, 40, 60, 70]
already_sorted = [5, 15, 25, 35, 45, 55]

# Exercise 3: Short unsorted list for tracing Insertion Sort
small_unsorted = [29, 10, 14, 37, 13]

# Exercise 4: List of student names for string sorting
student_names = ["Sardor", "Malika", "Aziz", "Dilnoza", "Jasur", "Kamola"]

# Exercise 5: Two sorted lists for testing the merge step
list_a = [3, 9, 15, 27]
list_b = [2, 8, 18, 20, 25]

# Exercise 6: List for tracing recursive Merge Sort
numbers_to_merge_sort = [38, 27, 43, 3, 9, 82, 10]

# Exercise 7: Benchmark lists
small_benchmark_list = [45, 12, 89, 34, 67, 23, 90, 11, 56, 78, 2, 99, 31, 84, 53, 19, 72, 41, 60, 15]

# 2,000 sorted unique integers
large_sorted_numbers = [10 + i * 3 for i in range(2000)]

# 2,000 unsorted integers (shuffled copy of large_sorted_numbers)
large_unsorted_numbers = list(large_sorted_numbers)
_rng.shuffle(large_unsorted_numbers)

# 2,000 reversed integers (worst case for simple quadratic sorts)
large_reversed_numbers = list(reversed(large_sorted_numbers))


# --- Structured datasets (for Exercise 8) ---

# Student academic records
students = [
    {"id": "U24101", "name": "Malika", "group": "CS-01", "gpa": 3.85, "exam_score": 92},
    {"id": "U24102", "name": "Aziz", "group": "CS-02", "gpa": 3.20, "exam_score": 74},
    {"id": "U24103", "name": "Dilnoza", "group": "CS-01", "gpa": 3.90, "exam_score": 95},
    {"id": "U24104", "name": "Sardor", "group": "CS-03", "gpa": 2.75, "exam_score": 68},
    {"id": "U24105", "name": "Jasur", "group": "CS-02", "gpa": 3.45, "exam_score": 81},
    {"id": "U24106", "name": "Kamola", "group": "CS-01", "gpa": 3.60, "exam_score": 88},
    {"id": "U24107", "name": "Bekzod", "group": "CS-03", "gpa": 3.10, "exam_score": 70},
    {"id": "U24108", "name": "Nigora", "group": "CS-02", "gpa": 3.95, "exam_score": 98},
    {"id": "U24109", "name": "Javohir", "group": "CS-01", "gpa": 2.90, "exam_score": 65},
    {"id": "U24110", "name": "Madina", "group": "CS-03", "gpa": 3.70, "exam_score": 88},
]

# Product catalog records
_categories = ["Electronics", "Books", "Clothing", "Home", "Sports"]
_item_templates = {
    "Electronics": ["Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"],
    "Books": ["Python Guide", "Algorithm Handbook", "Data Science 101", "Clean Code"],
    "Clothing": ["T-Shirt", "Hoodie", "Jacket", "Backpack"],
    "Home": ["Desk Lamp", "Ceramic Mug", "Water Bottle", "Notebook"],
    "Sports": ["Jump Rope", "Yoga Mat", "Dumbbell Set", "Gym Bag"]
}

products = []
for i in range(100):
    pid = 1001 + i
    cat = _categories[i % len(_categories)]
    item_list = _item_templates[cat]
    base_name = item_list[(i // len(_categories)) % len(item_list)]
    item_name = f"{base_name} #{pid}"
    price = round(10.0 + ((i * 17) % 90) + ((i % 5) * 0.99), 2)
    products.append({
        "id": pid,
        "name": item_name,
        "category": cat,
        "price": price
    })


if __name__ == "__main__":
    print("Dataset summary:")
    print(f" - small_numbers: {len(small_numbers)} elements")
    print(f" - nearly_sorted: {len(nearly_sorted)} elements")
    print(f" - already_sorted: {len(already_sorted)} elements")
    print(f" - small_unsorted: {len(small_unsorted)} elements")
    print(f" - student_names: {len(student_names)} elements")
    print(f" - list_a: {len(list_a)} elements, list_b: {len(list_b)} elements")
    print(f" - numbers_to_merge_sort: {len(numbers_to_merge_sort)} elements")
    print(f" - small_benchmark_list: {len(small_benchmark_list)} elements")
    print(f" - large_sorted_numbers: {len(large_sorted_numbers)} elements (min: {large_sorted_numbers[0]}, max: {large_sorted_numbers[-1]})")
    print(f" - large_unsorted_numbers: {len(large_unsorted_numbers)} elements")
    print(f" - large_reversed_numbers: {len(large_reversed_numbers)} elements")
    print(f" - students: {len(students)} student records")
    print(f" - products: {len(products)} product records")
    print("\nSample student record:")
    print(students[0])
    print("\nSample product record:")
    print(products[0])
