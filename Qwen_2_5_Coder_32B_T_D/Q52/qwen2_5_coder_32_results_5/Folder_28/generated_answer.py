def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 43
    for i in range(len(s) - n + 1):
        candidate = s[i:i + n]
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes