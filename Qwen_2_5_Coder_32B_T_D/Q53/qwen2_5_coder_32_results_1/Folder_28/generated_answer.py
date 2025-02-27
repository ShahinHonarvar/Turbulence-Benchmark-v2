import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    letters_only = re.findall('[a-z]+', s)
    for word in letters_only:
        length = len(word)
        if length >= 42:
            for i in range(length):
                for j in range(i + 42, length + 1):
                    substring = word[i:j]
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes