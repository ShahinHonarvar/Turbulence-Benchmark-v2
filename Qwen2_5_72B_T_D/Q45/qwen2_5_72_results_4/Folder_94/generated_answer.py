def palindromes_between_indices(s):
    chars = s[3:5].lower()
    char_freq = {}
    for char in chars:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    palindromes = set()
    for char, count in char_freq.items():
        if count >= 2:
            for middle_char in char_freq:
                if char_freq[middle_char] > 0:
                    palindrome = char + middle_char + char
                    palindromes.add(palindrome)
    return palindromes