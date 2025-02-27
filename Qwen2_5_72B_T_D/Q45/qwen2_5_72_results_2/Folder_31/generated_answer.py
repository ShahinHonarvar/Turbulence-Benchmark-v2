from collections import Counter
        from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9]
    letter_counts = Counter(filter(lambda x: x.isalpha(), substring.lower()))
    single_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    half_palindrome = ''.join([char * (count // 2) for char, count in letter_counts.items()])
    possible_palindromes = set()
    if len(single_chars) <= 1 and sum(letter_counts.values()) >= 6:
        for perm in permutations(half_palindrome):
            if len(perm) * 2 + len(single_chars) >= 6:
                half_perm = ''.join(perm)
                if single_chars:
                    palindrome = half_perm + single_chars[0] + half_perm[::-1]
                else:
                    palindrome = half_perm + half_perm[::-1]
                possible_palindromes.add(palindrome)
    return possible_palindromes