# level 1 - #1 - reverse negative integer
# def reverse_integer(n: int):
#     integer = str(n)
#     for i in integer:
#         if integer[0] == '-':
#             return int('-' + (integer[:0:-1]))
#         else:
#             return integer[::-1]
#
#
# print(reverse_integer(-123))
# print(reverse_integer(123))


# level 1 #2 - anagrams
# def are_anagrams(s1: str, s2: str):
#     if sorted(s1.lower()) == sorted(s2.lower()):
#         return True
#     else:
#         return False
#
#
# print(are_anagrams('care', 'race'))
# print(are_anagrams('hEArt', 'earth'))
# print(are_anagrams('rattle', 'battle'))


# level 2 #3 - reverse strings
def reverse_words(sentence: str):
    # Split the sentence into individual words using the .split() method
    sentence_list = [sentence.split()]
    # Create an empty list to store the reversed versions of words
    reverse_word_list = []
    # Iterate through each word in the list of words
    for word in sentence_list:
    # Reverse each word using string slicing with a step of -1
        reverse_word = word[::-1]
# Append the reversed word to the list of reversed words
        reverse_word_list.append(reverse_word)
# Join (.join) the reversed words back together into a single string, separated by spaces
        new_string = " ".join(reverse_word_list)
# Return the final reversed sentence
        return new_string


print(reverse_words('Katelyn Thornton'))


# level 2 task #4 - string of digits
def repeat_digits(s: str):
    result = ""  # Initialize an empty string to store the result

    for char in s:  # Iterate through each character in the input string
        current_number = int(char)  # Convert the character to an integer
        result = char * current_number  # Repeat the character based on its integer value

    return result  # Return the final result string


print(repeat_digits('456'))


# level 2 # 5 - vowel shortcut
vowels = ['a', 'e', 'i', 'o', 'u']


def shortcut(s: str):
    for i in s:
        if i not in vowels:
            result =


print(shortcut('test'))
print(shortcut('Katelyn Thornton'))
