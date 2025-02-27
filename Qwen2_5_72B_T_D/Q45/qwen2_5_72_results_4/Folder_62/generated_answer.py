from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:9]
    counter = Counter(substring.lower())
    odd_chars = [char for char, count in counter.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    else:
        if len(odd_chars) == 1:
            center = odd_chars[0]
            counter[center] -= 1
        else:
            center = ''
        half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
        result = set()
        if len(half_palindrome + center + half_palindrome[::-1]) >= 7:
            result.add(half_palindrome + center + half_palindrome[::-1])
        return result