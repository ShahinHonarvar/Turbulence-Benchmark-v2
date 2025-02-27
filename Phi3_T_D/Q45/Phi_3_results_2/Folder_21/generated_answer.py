from itertools import permutations

def palindromes_between_indices(s):
    char_count = {}
    for char in s[1:9].lower():
        char_count[char] = char_count.get(char, 0) + 1
    palindromes = set()
    odd_char = None

    def is_palindrome(s):
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True
    for char, count in char_count.items():
        if count % 2 == 1:
            if odd_char is not None:
                return set()
            odd_char = char
        palindromes.add(char * (count // 2))
    if not odd_char:
        palindromes_center = ['']
    else:
        palindromes_center = list(odd_char)
    center_permutations = list(permutations(palindromes_center))
    for center in center_permutations:
        temp = ''.join(center)
        for permutation in set(permutations(''.join(char_count.keys() * (count // 2)))):
            palindrome = ''.join(permutation) + ''.join(center)[::-1]
            if len(palindrome) >= 7 and is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes