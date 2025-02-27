from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    result = set()

    def generate_palindromes(half, length):
        if len(odd_chars) > 1:
            return
        if len(odd_chars) == 1:
            center = odd_chars[0]
        else:
            center = ''
        palindrome = half + center + half[::-1]
        if len(palindrome) >= 5:
            result.add(palindrome)

    def backtrack(path, chars):
        if len(path) > (len(substring) - len(odd_chars)) // 2:
            return
        if len(path) == (len(substring) - len(odd_chars)) // 2:
            generate_palindromes(path, len(substring))
            return
        for char in chars:
            if chars[char] > 1:
                chars[char] -= 2
                backtrack(path + char, chars)
                chars[char] += 2
    if len(odd_chars) > 1:
        return set()
    backtrack('', char_count)
    return result