import string

def palindromes_of_specific_lengths(s):
    letters = set(string.ascii_lowercase)
    s = s[30:85].lower()
    palindromes = set()
    for i in range(len(s) - 11):
        for j in range(i + 11, min(i + 20, len(s)) + 1):
            sub = s[i:j]
            if set(sub).issubset(letters) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes