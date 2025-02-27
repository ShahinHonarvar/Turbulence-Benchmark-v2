def palindromes_between_indices(s):
    substring = s[2:4].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    palindromes = set()
    for char, count in char_count.items():
        if count >= 2:
            for i in range(97, 123):
                middle_char = chr(i)
                palindrome = char + middle_char + char
                palindromes.add(palindrome)
    return palindromes