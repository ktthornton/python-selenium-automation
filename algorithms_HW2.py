# level 1 - #1 - reverse negative integer
def reverse_integer(n: int):
    integer = str(n)
    return int('-' + (integer[:0:-1]))


print(reverse_integer(-123))
print(reverse_integer(-189))


# level 1 #2 - anagrams
def are_anagrams(s1: str, s2: str):
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    else:
        return False


print(are_anagrams('care', 'race'))
print(are_anagrams('hEArt', 'earth'))
print(are_anagrams('rattle', 'battle'))


# level 2 #3 - reverse strings
def reverse_words(sentence: str):
    # Split the sentence into individual words using the .split() method
    split_sentence = sentence.split()
    # Create an empty list to store the reversed versions of words
    result = []
    # Iterate through each word in the list of words
    for word in split_sentence:
    # Reverse each word using string slicing with a step of -1
    # Append the reversed word to the list of reversed words
        result.append(word[::-1])
    # Join (.join) the reversed words back together into a single string, separated by spaces
    # Return the final reversed sentence
    return " ".join(result)


test_sentence = 'My name is Katelyn Thornton'
print(reverse_words(test_sentence))


# level 2 task #4 - string of digits
def repeat_digits(s: str):
    result = ""  # Initialize an empty string to store the result

    for i in range(len(s)):  # Iterate through each character in the input string
          result += int(s[i]) * s[i]
          # Convert the character to an integer
          # Repeat the character based on its integer value

    return result  # Return the final result string


print(repeat_digits('0123'))
print(repeat_digits('456'))


# level 2 # 5 - vowel shortcut
vowels = ['a', 'e', 'i', 'o', 'u']


def shortcut(s: str):
    result = ''
    for i in range(len(s)):
        if s[i] not in vowels:
            result += s[i]
    return result


print(shortcut('hello'))
print(shortcut('goodbye'))
