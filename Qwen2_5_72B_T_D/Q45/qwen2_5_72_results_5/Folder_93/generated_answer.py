from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:8].lower()
    char_count = Counter(substring)
    even_chars = {char: count for char, count in char_count.items() if count % 2 == 0}
    odd_chars = {char: count for char, count in char_count.items() if count % 2 != 0}
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in even_chars.items()))
    if odd_chars:
        half_palindrome += next(iter(odd_chars))
    palindromes = set()
    for length in range(6, 7 + 1):
        if len(half_palindrome) * 2 - len(odd_chars) >= length:
            palindromes.add(half_palindrome[:length // 2] + half_palindrome[length // 2:][::-1])
    return palindromes