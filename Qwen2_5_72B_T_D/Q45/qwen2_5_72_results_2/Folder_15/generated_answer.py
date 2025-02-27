def palindromes_between_indices(s):
    substring = s[1:3].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    palindromes = set()
    for char, count in char_freq.items():
        if count >= 2:
            for char2, count2 in char_freq.items():
                if char2 != char and count2 >= 1:
                    pal = char + char2 + char
                    palindromes.add(pal)
    return palindromes