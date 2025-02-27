def palindromes_between_indices(s):
    sub_str = s[2:4].lower()
    char_freq = {}
    for char in sub_str:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    palindromes = set()
    for char, freq in char_freq.items():
        if freq > 1:
            for other_char, other_freq in char_freq.items():
                if other_char != char and other_freq > 0:
                    if freq // 2 >= 1:
                        palindrome = char + other_char + char
                        palindromes.add(palindrome)
    return palindromes