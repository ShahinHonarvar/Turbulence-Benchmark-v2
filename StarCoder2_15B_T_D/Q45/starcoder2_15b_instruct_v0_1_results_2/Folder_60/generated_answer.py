import re

def palindromes_between_indices(string):
    pattern = '[a-zA-Z]'
    letters = re.findall(pattern, string)
    palindromes = set()
    for i in range(3, 7):
        for j in range(i + 1, 7):
            for k in range(j, 7):
                palindrome = letters[i] + letters[j] + letters[k]
                if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes