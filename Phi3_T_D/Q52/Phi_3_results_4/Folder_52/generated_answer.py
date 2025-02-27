def palindrome_of_length_n(s):
    n = 423
    s = s.lower()
    length = len(s)
    if length < n:
        return set()
    palindromes = set()
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes