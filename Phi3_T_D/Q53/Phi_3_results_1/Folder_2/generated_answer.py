def palindrome_of_length_at_least_n(s):
    length = 55
    strings_set = {i for i in s.lower().split() if i.isalpha()}
    return {word for word in strings_set if len(word) >= length and word == word[::-1]}