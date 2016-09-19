my_sentence = "the blue dog decided to find it's way home"

my_counter_dictionary = {}

# defaultdict

for letter in my_sentence:
    if letter in my_counter_dictionary.keys():
        my_counter_dictionary[letter] += 1
    else:
        my_counter_dictionary[letter] = 1

print(sorted(my_counter_dictionary.items(), key=lambda x: x[1]))
