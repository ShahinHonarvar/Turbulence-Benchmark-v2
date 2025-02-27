def palindromes_of_specific_lengths(s):
    valid_range = s[:301]
    palindromes = set()
    for i in range(len(valid_range)):
        for j in range(i + 50, min(i + 61, len(valid_range) + 1)):
            substring = valid_range[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes