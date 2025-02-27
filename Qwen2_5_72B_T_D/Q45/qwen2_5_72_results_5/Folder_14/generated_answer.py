def palindromes_between_indices(s):
    sub_str = s[4:6].lower()
    char_freq = {}
    for char in sub_str:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    palindromes = set()
    for center, freq in char_freq.items():
        if freq >= 2:
            for side, side_freq in char_freq.items():
                if side != center and side_freq >= 1:
                    palindrome = side + center * (freq // 2 * 2) + side
                    if len(palindrome) >= 3:
                        palindromes.add(palindrome)
    return palindromes