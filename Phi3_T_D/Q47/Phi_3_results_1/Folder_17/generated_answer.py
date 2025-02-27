def palindromes_of_specific_lengths(s):
    selected_slice = s[22:97]
    palindromes = set()
    for length in range(52, 56):
        for start in range(len(selected_slice) - length + 1):
            substring = selected_slice[start:start + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes