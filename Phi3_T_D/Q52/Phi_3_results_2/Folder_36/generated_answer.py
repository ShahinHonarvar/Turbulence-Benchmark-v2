def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 337):
        candidate = s[i:i + 338]
        if candidate == candidate[::-1]:
            palindromes.add(candidate.lower())
    return palindromes