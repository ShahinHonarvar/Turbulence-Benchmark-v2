from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    possible_palindromes = set()
    if len(odd_chars) <= 1:
        if len(substring) < 3:
            return set()
        elif len(substring) == 3:
            for char in char_count:
                if char_count[char] >= 2:
                    possible_palindromes.add(char * 2 + char)
        else:
            for permutation in permutations(char_count, len(substring) // 2):
                middle = odd_chars[0] if odd_chars else ''
                palindrome = permutation + middle + permutation[::-1]
                if all((palindrome.count(char) <= count for char, count in char_count.items())):
                    possible_palindromes.add(palindrome)
    return possible_palindromes

def permutations(char_count, length):
    if length == 0:
        return ['']
    perms = []
    for char in char_count:
        if char_count[char] > 0:
            char_count[char] -= 1
            for perm in permutations(char_count, length - 1):
                perms.append(char + perm)
            char_count[char] += 1
    return perms