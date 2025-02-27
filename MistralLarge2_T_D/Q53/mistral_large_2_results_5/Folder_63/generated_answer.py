import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string).lower()
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 37, length + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes