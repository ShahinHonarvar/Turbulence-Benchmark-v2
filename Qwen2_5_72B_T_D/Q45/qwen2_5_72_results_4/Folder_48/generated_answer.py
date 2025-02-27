from collections import Counter

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    else:
        half_palindrome = ''.join((char * (count // 2) for char, count in char_count.items()))
        if odd_chars:
            middle_char = odd_chars[0]
        else:
            middle_char = ''
        palindromes = set()
        if len(half_palindrome) * 2 + len(middle_char) >= 4:
            for permutation in set([''.join(p) for p in itertools.permutations(half_palindrome + middle_char)]):
                if len(permutation) >= 2:
                    palindrome = permutation + permutation[-2::-1]
                    palindromes.add(palindrome)
        return palindromes