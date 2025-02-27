def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 115, length + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes