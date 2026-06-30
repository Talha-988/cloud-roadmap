marks = [45, 80, 67, 92, 55]
print(f"Maximum marks are {max(marks)}")
print(f"Minimum marks are {min(marks)}")
print(f"Total students are {len(marks)}")
marks.sort()
print(f"Ascending marks are {marks}")
marks.sort(reverse=True)
print(f"Descending marks are {marks}")