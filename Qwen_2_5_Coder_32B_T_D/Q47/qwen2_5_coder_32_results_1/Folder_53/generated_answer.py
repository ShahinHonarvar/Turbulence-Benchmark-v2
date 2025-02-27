def palindromes_of_specific_lengths(s):
    s = s[1:300]
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 11, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                palindromes.add(substr.lower())
    return palindromes