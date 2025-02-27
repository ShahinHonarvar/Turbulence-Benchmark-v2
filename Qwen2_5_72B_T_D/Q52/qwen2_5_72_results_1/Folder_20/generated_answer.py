def palindrome_of_length_n(s):
    s = s.lower()
    n = 53
    palindromes = set()
    for i in range(len(s) - n + 1):
        candidate = s[i:i + n]
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes