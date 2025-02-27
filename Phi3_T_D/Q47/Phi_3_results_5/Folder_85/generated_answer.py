def palindromes_of_specific_lengths(s):
    sub_string = s[29:99]
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(sub_string) - length + 1):
            candidate = sub_string[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate.lower())
    return palindromes