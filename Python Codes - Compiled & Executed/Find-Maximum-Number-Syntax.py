#Python Program to Find the Maximum Number from a given List:

list_of_scores = [100, 200, 89, 76, 900, 1754, 7351, 8981, 6413, 99999]
max_score = 0
for score in list_of_scores:
    if score > max_score:
        max_score = score

print(f"Maximum Number in Given Range is: {max_score}")
