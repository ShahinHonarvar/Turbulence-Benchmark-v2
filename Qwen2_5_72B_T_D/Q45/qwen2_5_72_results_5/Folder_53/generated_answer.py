from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    else:
        half_palindrome = ''.join([char * (count // 2) for char, count in char_count.items()])
        possible_palindromes = set()
        for permutation in set([''.join(p) for p in itertools.permutations(half_palindrome)]):
            if odd_chars:
                palindrome = permutation + odd_chars[0] + permutation[::-1]
            else:
                palindrome = permutation + permutation[::-1]
            if len(palindrome) >= 6:
                possible_palindromes.add(palindrome)
        return possible_palindromes