# 1. Write a function `make_dictionary` that takes two lists and returns a
# dictionary with the names as keys and the scores as values.
def make_dictionary(keys_list, values_list):
    i=0
    dictionary = {}
    for thing in keys_list:
        dictionary[thing] = values_list[i]
        i += 1
    return dictionary
print(make_dictionary(["a", "b"], [1, 2]))
print(make_dictionary([1, 2, 3], [5, 6, 7]))
print(make_dictionary(["a", "b", "c", "b"], ["apple", "banana", "clementine", "date"]))
print(make_dictionary(["key"], ["value"]))

# # You have been given the following list fo students and their test scores:
names = ["Maria", "Nushi", "Mohammed", "Jose", "Wei"]
scores = [10, 23, 13, 18, 12]

# # Assign the result of make_dictionary to score_dict, which will be used in the
# # exercises that follow.
score_dict = make_dictionary(names, scores)

# # 2. Using `score_dict`, find the score for "Nushi"
# #### YOUR CODE HERE

print(score_dict["Nushi"])

# # 3. Add a score 19 for "John"
# #### YOUR CODE HERE

score_dict["John"] = 19
print(score_dict)

# # 4. Calculate the average of all the scores in `score_dict`
# #### YOUR CODE HERE
scores_list = list(score_dict.values())
print(scores_list)
scores_added = 0
count = 0
for value in scores_list:
    scores_added += int(value)
    count += 1
print(scores_added/count)
# # 5. Update the score for "Wei" to be 13
# #### YOUR CODE HERE

score_dict["Wei"] = 13
print(score_dict)

# # 6. Nushi has just dropped this class. Delete "Nushi" and his score from
# # `score_dict`
# #### YOUR CODE HERE

del score_dict["Nushi"]
print(score_dict)