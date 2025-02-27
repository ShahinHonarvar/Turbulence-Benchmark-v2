def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 115, len(s) + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes