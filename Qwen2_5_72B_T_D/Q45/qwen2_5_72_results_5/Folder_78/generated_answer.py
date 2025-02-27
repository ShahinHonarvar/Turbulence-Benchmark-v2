def palindromes_between_indices(s):
    substring = s[6:9].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    palindromes = set()
    for char, count in char_freq.items():
        if count >= 2:
            palindromes.add(char * 3)
        if count >= 4:
            palindromes.add(char * 2 + char)
    return palindromes