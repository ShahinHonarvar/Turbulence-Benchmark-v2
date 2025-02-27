import string

def palindromes_between_indices(s):
    letters = [c for c in s if c in string.ascii_letters]
    palindromes = set()
    for i in range(len(letters) - 6):
        for j in range(i + 6, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes