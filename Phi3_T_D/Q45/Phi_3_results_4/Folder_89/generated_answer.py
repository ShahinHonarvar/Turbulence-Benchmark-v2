from itertools import permutations

def palindromes_between_indices(s):
    start, end = (5, 9)
    substring = s[start:end + 1].lower()
    letter_count = {}
    for letter in substring:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    palindromes = set()
    for length in range(6, end - start + 1 + 1, 2):
        for perm in permutations(letter_count.keys(), length // 2):
            half_palindrome = ''.join(perm)
            if length % 2 == 0:
                palindrome = half_palindrome + half_palindrome[::-1]
            else:
                for letter, count in letter_count.items():
                    if count > 0:
                        palindrome = half_palindrome + letter + half_palindrome[::-1]
                        letter_count[letter] -= 1
                        break
                else:
                    continue
            if len(palindrome) == length and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes