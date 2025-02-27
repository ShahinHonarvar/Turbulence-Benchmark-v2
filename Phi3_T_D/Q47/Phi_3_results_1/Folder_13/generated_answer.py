def palindromes_of_specific_lengths(s):
    sub_s = s[13:96]
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(sub_s) - length + 1):
            candidate = sub_s[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes