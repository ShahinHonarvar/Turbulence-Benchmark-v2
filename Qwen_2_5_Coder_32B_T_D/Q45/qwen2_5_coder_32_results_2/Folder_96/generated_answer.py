from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if c in string.ascii_lowercase]
    count = Counter(letters)
    half_length = 6 // 2

    def can_form_palindrome(count):
        odd_count = sum((1 for v in count.values() if v % 2 != 0))
        return odd_count <= 1

    def generate_half_palindrome(count):
        half = []
        for char, freq in count.items():
            half.extend(char * (freq // 2))
        return half
    palindromes = set()
    if can_form_palindrome(count):
        half = generate_half_palindrome(count)
        for half_perm in set(permutations(half, half_length)):
            half_str = ''.join(half_perm)
            if 6 % 2 == 0:
                palindrome = half_str + half_str[::-1]
            else:
                middle_char = [char for char, freq in count.items() if freq % 2 != 0]
                palindrome = half_str + (middle_char[0] if middle_char else '') + half_str[::-1]
            palindromes.add(palindrome)
    return palindromes