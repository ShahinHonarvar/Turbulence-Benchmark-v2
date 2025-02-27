def palindromes_of_specific_lengths(s):
    s = s[11:98]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 29, i + 63):
            if j > len(s):
                continue
            candidate = s[i:j]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes