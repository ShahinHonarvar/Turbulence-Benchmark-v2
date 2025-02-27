from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:10].lower()
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    potential_palindromes = set()
    for perm in permutations(letter_counts.items()):
        half = ''
        middle = ''
        for char, count in perm:
            half += char * (count // 2)
            if count % 2 != 0 and middle == '':
                middle = char
        for i in range(3, len(half) + 1):
            if 2 * i + (middle != '') >= 7:
                palindrome = half[:i] + middle + half[:i][::-1]
                potential_palindromes.add(palindrome)
    return potential_palindromes