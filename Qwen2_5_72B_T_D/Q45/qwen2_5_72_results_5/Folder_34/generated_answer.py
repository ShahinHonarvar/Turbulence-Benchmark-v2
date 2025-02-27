from itertools import permutations

def palindromes_between_indices(s):
    substr = s[5:8]
    char_freq = {}
    for char in substr:
        if char.isalpha():
            char = char.lower()
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    potential_palindromes = set()
    for perm in permutations(char_freq.items()):
        half = ''.join([char * (count // 2) for char, count in perm])
        if any((count % 2 for _, count in perm)):
            for char, _ in perm:
                potential_palindromes.add((half + char + half[::-1]).lower())
        else:
            potential_palindromes.add((half + half[::-1]).lower())
    return {palindrome for palindrome in potential_palindromes if len(palindrome) >= 4}