from pprint import pprint

# Delete the empty spaces from a string and return a list of the chars
my_string = "Hello world this is my string"
list_of_chars = [*my_string.replace(" ","").lower()]
print(list_of_chars)

# Count in a dictionary how many of each chars are in a given string
chars_dict = {}
for char in list_of_chars:
    if char in chars_dict:
        chars_dict[char] += 1
    else:
        chars_dict[char] = 1

pprint(chars_dict, width=1)

# Sort the keys in a dictrionary by the content of its value. Return a list of tuples
tuples_sorted = sorted(chars_dict.items(), key=lambda key: key[1], reverse=True )
print(tuples_sorted)

# From a list  of tuples, return the tuples which have the higher value
higher_value = tuples_sorted[0][1]
max_values_in_list = []

for item in tuples_sorted:
    if item[1] == higher_value:
        max_values_in_list.append(item)
    else:
        break

print(max_values_in_list)

# Create a message that says '
# The characters which has more repetitions (3) are:
# C
# D '
print(f"The characters with highest repetitions ({higher_value}) are:")
for item in max_values_in_list:
    char = item[0].upper()
    print(f"- {char}")
