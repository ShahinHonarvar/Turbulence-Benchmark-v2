def palindromes_of_specific_lengths(s):
    s_subsection = s[44:100]
    min_length, max_length = (13, 42)
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(len(s_subsection) - length + 1):
            substring = s_subsection[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes