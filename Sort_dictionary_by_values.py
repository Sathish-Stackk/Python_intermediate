marks = {
    "Ravi": 85,
    "Kiran": 92,
    "Arun": 78,
    "Manoj": 89
}

sorted_marks = dict(sorted(marks.items(),
                           key=lambda x: x[1]))

print("Sorted Marks:", sorted_marks)
