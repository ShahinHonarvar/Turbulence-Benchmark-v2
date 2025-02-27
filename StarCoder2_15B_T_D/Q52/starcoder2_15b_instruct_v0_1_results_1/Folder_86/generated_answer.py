import re

def palindrome_of_length_n(string):
    substrings = set()
    n = 181
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            substrings.add(substring)
    return substrings