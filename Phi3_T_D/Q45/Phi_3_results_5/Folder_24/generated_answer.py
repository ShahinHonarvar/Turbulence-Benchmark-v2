from itertools import permutations

def palindromes_between_indices(text):
    substring = text[2:10].lower()
    chars = {}
    for char in substring:
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    palindromes = set()
    for size in range(4, min(len(substring), 10) // 2 + 1):
        for combo in permutations(chars.keys(), size):
            left_half = ''.join(sorted(combo))
            palindrome = left_half + left_half[::-1][1:]
            if palindrome[::-1] == palindrome:
                palindromes.add(palindrome)
    return palindromes