def palindromes_between_indices(s):
    sl = s[1:7]
    char_count = {}
    for char in sl:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    def find_palindromes(chars, current='', length=3):
        if length > len(chars) or len(chars) == 0:
            return set()
        if len(current) >= length and current == current[::-1]:
            return {current}
        palindromes = set()
        for char in chars:
            if chars[char] > 0:
                chars[char] -= 1
                palindromes |= find_palindromes(chars, current + char, length)
                chars[char] += 1
        return palindromes
    result = find_palindromes(char_count)
    return result