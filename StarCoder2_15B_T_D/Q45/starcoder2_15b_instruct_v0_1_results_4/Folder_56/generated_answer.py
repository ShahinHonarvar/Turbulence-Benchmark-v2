import re

def palindromes_between_indices(string):
    pattern = '[a-zA-Z]'
    letters = re.findall(pattern, string)
    palindromes = []
    for i in range(len(letters) - 4):
        window = letters[i:i + 5]
        for j in range(i + 1, len(letters) - 3):
            window += letters[j:j + 5]
        for k in range(i + 2, len(letters) - 2):
            window += letters[k:k + 5]
        for l in range(i + 3, len(letters) - 1):
            window += letters[l:l + 5]
        for m in range(i + 4, len(letters)):
            window += letters[m:m + 5]
    for palindrome in window:
        if palindrome.lower() == palindrome[::-1].lower():
            palindromes.append(palindrome)
    return set(palindromes)