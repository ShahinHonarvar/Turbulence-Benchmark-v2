def palindromes_of_specific_lengths(s):
    s = s[:10]
    palindromes = set()
    for size in range(3, 6):
        for i in range(len(s) - size + 1):
            substr = s[i:i + size]
            if all((c.isalpha() for c in substr)):
                substr = substr.lower()
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes