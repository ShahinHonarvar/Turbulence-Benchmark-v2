def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 278):
        candidate = s[i:i + 279]
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes