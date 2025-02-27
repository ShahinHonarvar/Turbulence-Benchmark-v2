import re

def palindromes_between_indices(text):
    letters = re.findall('[a-zA-Z]', text)
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 5, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes