from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    odd_count_letters = [letter for letter, count in letter_counts.items() if count % 2 != 0]
    if len(odd_count_letters) > 1:
        return set()
    available_letters = [letter for letter, count in letter_counts.items() for _ in range(count // 2)]
    if len(available_letters) < 3:
        return set()
    possible_palindromes = set()
    for perm in set(permutations(available_letters)):
        half_palindrome = ''.join(perm)
        if odd_count_letters:
            full_palindrome = half_palindrome + odd_count_letters[0] + half_palindrome[::-1]
        else:
            full_palindrome = half_palindrome + half_palindrome[::-1]
        if len(full_palindrome) >= 7:
            possible_palindromes.add(full_palindrome)
    return possible_palindromes