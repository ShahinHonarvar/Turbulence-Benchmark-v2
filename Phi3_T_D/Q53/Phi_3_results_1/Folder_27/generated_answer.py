from collections import defaultdict

def extend_palindrome(string, left, right, palindromes):
    while left >= 0 and right < len(string) and (string[left].lower() == string[right].lower()):
        if right - left + 1 >= 100:
            palindromes.add(string[left:right + 1].upper())
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    char_index_map = defaultdict(list)
    for i, c in enumerate(s.lower()):
        if c.isalpha():
            char_index_map[c].append(i)
    palindromes = set()
    for c, indices in char_index_map.items():
        for left in indices:
            right = left
            extend_palindrome(s, left, right, palindromes)
    return palindromes