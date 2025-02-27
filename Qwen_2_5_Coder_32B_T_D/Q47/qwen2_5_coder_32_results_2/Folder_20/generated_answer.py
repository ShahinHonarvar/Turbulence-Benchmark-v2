import string

def palindromes_of_specific_lengths(s):
    letters = set(string.ascii_letters)
    s = s[20:75].lower()
    palindromes = set()
    for i in range(len(s) - 35):
        for j in range(i + 35, min(i + 42, len(s)) + 1):
            substr = s[i:j]
            if set(substr).issubset(letters) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes