from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:6]
    counter = Counter(substring.lower())
    middle = ''
    char_list = []
    for char, count in counter.items():
        if count % 2 != 0:
            if not middle:
                middle = char
            elif count > 1:
                char_list.extend([char] * (count - 1))
        else:
            char_list.extend([char] * count)
    half_palindrome = ''.join(char_list[:len(char_list) // 2])
    palindromes = set()
    if middle:
        full_palindrome = half_palindrome + middle + half_palindrome[::-1]
        if len(full_palindrome) >= 6:
            palindromes.add(full_palindrome)
    elif len(half_palindrome) >= 3:
        full_palindrome = half_palindrome + half_palindrome[::-1]
        palindromes.add(full_palindrome)
    return palindromes