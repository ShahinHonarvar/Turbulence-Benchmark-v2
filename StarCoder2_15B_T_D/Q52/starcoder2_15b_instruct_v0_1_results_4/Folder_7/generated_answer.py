import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 415):
        substring = string[i:i + 416]
        substring = re.sub('[^a-zA-Z]', '', substring)
        is_palindrome = True
        for j in range(len(substring) // 2):
            if substring[j].lower() != substring[-j - 1].lower():
                is_palindrome = False
                break
        if is_palindrome:
            palindromes.add(substring)
    return palindromes