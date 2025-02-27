import re

def palindrome_of_length_n(s):
    s = s.lower()
    letters = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(letters) - 28):
        substring = letters[i:i + 29]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes