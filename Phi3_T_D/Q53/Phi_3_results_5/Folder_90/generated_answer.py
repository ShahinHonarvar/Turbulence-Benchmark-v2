from collections import Counter

def palindrome_of_length_at_least_n(text):
    n = 140
    text = text.lower()
    half_n = n // 2
    find_palindromes = set()
    for center in range(len(text)):
        for radius in range(half_n):
            left, right = (center - radius, center + radius + 1)
            if right >= len(text) or left < 0:
                break
            sub_str = text[left:right]
            if sub_str == sub_str[::-1] and len(sub_str) >= n:
                find_palindromes.add(sub_str.upper())
            elif Counter(sub_str[:half_n]) == Counter(sub_str[:half_n][::-1]):
                find_palindromes.add(sub_str[half_n:-half_n].upper())
    return find_palindromes