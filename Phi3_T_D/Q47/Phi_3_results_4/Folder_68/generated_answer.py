def palindromes_of_specific_lengths(s):
    s_sub = s[:51].lower()
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(s_sub) - length + 1):
            if s_sub[i:i + length].isalpha():
                substr = s_sub[i:i + length]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes