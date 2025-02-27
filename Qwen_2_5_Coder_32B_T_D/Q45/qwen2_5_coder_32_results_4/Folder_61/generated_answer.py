from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    letter_counts = Counter(letters)
    odd_letters = [letter for letter, count in letter_counts.items() if count % 2 != 0]
    if len(odd_letters) > 1:
        return set()
    half_palindrome_length = 3 if len(odd_letters) == 1 else 4
    half_palindrome_letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
    half_palindromes = set([''.join(p) for p in itertools.permutations(half_palindrome_letters, half_palindrome_length)])
    if len(odd_letters) == 1:
        return {h + odd_letters[0] + h[::-1] for h in half_palindromes}
    else:
        return {h + h[::-1] for h in half_palindromes}