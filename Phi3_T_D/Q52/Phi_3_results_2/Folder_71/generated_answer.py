def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 77):
        candidate = s[i:i + 78]
        if candidate == candidate[::-1] and candidate.isalpha():
            palindromes.add(candidate)
    return palindromes