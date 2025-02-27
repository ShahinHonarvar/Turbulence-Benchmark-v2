def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    all_palindromes = set()
    for center in range(len(s)):
        for radius in range(min(len(s) - center, 49) // 2):
            substr = s[center - radius:center + radius + 1]
            if substr.isalpha() and substr == substr[::-1]:
                all_palindromes.add(substr)
    filtered_palindromes = set(filter(lambda s: 13 <= len(s) <= 49, all_palindromes))
    return filtered_palindromes