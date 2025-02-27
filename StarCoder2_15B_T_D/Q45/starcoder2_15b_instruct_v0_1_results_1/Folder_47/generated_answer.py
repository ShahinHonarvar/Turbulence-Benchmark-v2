import re

def palindromes_between_indices(string):
    sub_string = string[3:8]
    letters = re.findall('[a-zA-Z]', sub_string)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i].lower() + letters[j].lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes