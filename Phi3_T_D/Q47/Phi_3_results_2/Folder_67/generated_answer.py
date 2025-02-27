def palindromes_of_specific_lengths(s):
    base_string = s[65:99]
    palindromes = set()
    for center in range(len(base_string)):
        for radius in range(1, min(max(0, 26 - center), (33 - center) // 2 + 1)):
            substring = base_string[center - radius:center + radius + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes