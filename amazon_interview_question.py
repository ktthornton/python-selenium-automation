# Create a function that will take a string as an input and return the 1st unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

def unique_letter(string: str):
    string = string.lower() # will eliminate capital letters being identified as a unique letter

    unique_letter_dict = {}

    for letter in string:
        if letter not in unique_letter_dict:
            unique_letter_dict[letter] = 1
        else:
            unique_letter_dict[letter] += 1

    for k, v in unique_letter_dict.items():
        if v == 1:
            return k


print(unique_letter('google'))
print(unique_letter('GoOgle'))
print(unique_letter('')) # answers None
print(unique_letter('gogo')) # answers None
print(unique_letter(6565))


# complexity of this algorithm is O(n)
