import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[7:10])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes