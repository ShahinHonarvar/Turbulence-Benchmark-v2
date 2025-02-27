def palindromes_of_specific_lengths(s):
    s = s[101:293].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(max(i + 153, len(s)), min(i + 183, len(s)) + 1):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes