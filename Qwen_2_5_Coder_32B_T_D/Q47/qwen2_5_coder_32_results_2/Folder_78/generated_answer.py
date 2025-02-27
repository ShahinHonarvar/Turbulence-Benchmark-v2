def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    palindromes = set()
    for start in range(len(s) - 18):
        for end in range(start + 18, min(start + 55, len(s))):
            candidate = s[start:end + 1]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes