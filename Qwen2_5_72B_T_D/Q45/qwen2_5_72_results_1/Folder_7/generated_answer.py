from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[1:10]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    letter_counts = Counter(letters)
    available_letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
    palindromes = set()
    for length in range(7, len(available_letters) * 2 + 2):
        for perm in permutations(available_letters, length // 2):
            half_palindrome = ''.join(perm)
            if length % 2 == 0:
                palindrome = half_palindrome + half_palindrome[::-1]
            else:
                for center in letter_counts:
                    if letter_counts[center] % 2 != 0:
                        palindrome = half_palindrome + center + half_palindrome[::-1]
                        break
            if is_palindrome(palindrome) and len(palindrome) >= 7:
                palindromes.add(palindrome)
    return palindromes