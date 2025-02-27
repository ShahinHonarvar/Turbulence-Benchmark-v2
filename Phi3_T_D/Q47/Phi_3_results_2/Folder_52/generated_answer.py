def palindromes_of_specific_lengths(s):
    sub_str = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(sub_str) - length + 1):
            candidate = sub_str[i:i + length]
            if all((c.isalpha() for c in candidate)) and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate.lower())
    return palindromes