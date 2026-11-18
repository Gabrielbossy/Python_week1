def full_name(first, last):
    return(first + " " + last).title()


print(full_name("gabRieL", "otiEno"))
    
def calculate_average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)

scores = [60, 70, 80]
print(calculate_average(scores))    # 70.0
print(calculate_average([1, 2, 3])) # 2.0