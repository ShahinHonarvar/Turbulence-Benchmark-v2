from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    char_count = Counter(s)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    even_chars = [char for char, count in char_count.items() if count % 2 == 0]
    if len(odd_chars) > 1 or len(s) < 5:
        return set()
    half_palindrome = []
    for char in even_chars:
        half_palindrome.extend([char] * (char_count[char] // 2))
    if odd_chars:
        half_palindrome.append(odd_chars[0])
    half_palindrome = ''.join(half_palindrome)
    if len(half_palindrome) * 2 - 1 < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(half_palindrome)):
        if len(perm) >= 3:
            palindrome = perm[:len(perm) // 2] + perm[len(perm) // 2] * (len(perm) % 2) + perm[:len(perm) // 2][::-1]
            palindromes.add(''.join(palindrome))
    return {p for p in palindromes if len(p) >= 5}