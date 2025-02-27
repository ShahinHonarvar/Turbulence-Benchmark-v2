def palindromes_between_indices(s):
    substring = s[7:9].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    palindromes = set()
    for center, freq in char_freq.items():
        if freq >= 2:
            for side, side_freq in char_freq.items():
                if side != center and side_freq >= 1:
                    palindrome = side + center * (freq // 2) + side
                    palindromes.add(palindrome + palindrome[::-1])
    return {p for p in palindromes if len(p) >= 3}