import re

def palindromes_between_indices(text):
    letters = re.findall('[a-zA-Z]', text[2:6])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes