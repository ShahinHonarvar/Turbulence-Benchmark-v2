from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    freq = Counter(substring)
    odd_counts = [char for char, count in freq.items() if count % 2 != 0]
    if len(odd_counts) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in freq.items()))
    palindromes = set()

    def generate_palindromes(half, chars):
        if not chars:
            palindrome = half + half[::-1]
            for length in range(6, 13):
                palindromes.add(palindrome[:length // 2] + (chars[0] if chars else '') + palindrome[length // 2:])
            return
        for i in range(len(chars)):
            new_half = half + chars[i]
            new_chars = chars[:i] + chars[i + 1:]
            generate_palindromes(new_half, new_chars)
    generate_palindromes('', list(half_palindrome))
    return palindromes