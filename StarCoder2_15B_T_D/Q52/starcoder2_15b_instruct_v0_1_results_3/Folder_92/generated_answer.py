import re

def palindrome_of_length_n(string):
    n = 10
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            matches = re.findall('[a-zA-Z]+', substring)
            if matches:
                result.add(''.join(matches).lower())
    return result