from itertools import permutations

def palindromes_between_indices(s):
    middle = s[2:7].lower()
    letter_counts = {}
    for letter in middle:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    min_odd_count = 0
    for count in letter_counts.values():
        if count % 2 == 1:
            min_odd_count += 1
            if min_odd_count > 1:
                return set()
    if min_odd_count == 1:
        middle_length = len(middle)
        for letter, count in letter_counts.items():
            letter_counts[letter] = (count + 1) // 2
        half_palindromes = [letter * (count // 2) for letter, count in letter_counts.items()]
        half_palindromes.sort()
        palindromes = set()
        for perm in permutations(half_palindromes):
            palindrome = ''.join(perm) + middle[middle_length // 2] * min_odd_count + ''.join(reversed(perm))
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
        return palindromes
    half_length = (len(middle) - min_odd_count) // 2
    half_palindromes = [letter * (count // 2) for letter, count in letter_counts.items()]
    half_palindromes.sort()
    palindromes = {''.join(perm) + ''.join(reversed(perm)) for perm in permutations(half_palindromes)}
    return set((p for p in palindromes if len(p) >= 5))