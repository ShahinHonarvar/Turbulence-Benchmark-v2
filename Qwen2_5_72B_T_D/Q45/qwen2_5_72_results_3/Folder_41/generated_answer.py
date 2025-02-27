def palindromes_between_indices(s):
    substring = s[2:4].lower()
    char_freq = {}
    for char in substring:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    result = set()
    for char in char_freq:
        if char_freq[char] >= 2:
            for i in range(65, 91):
                middle_char = chr(i)
                if char_freq.get(middle_char.lower(), 0) > 0:
                    palindrome = char + middle_char + char
                    result.add(palindrome)
        if char_freq[char] >= 3:
            palindrome = char * 3
            result.add(palindrome)
    return result