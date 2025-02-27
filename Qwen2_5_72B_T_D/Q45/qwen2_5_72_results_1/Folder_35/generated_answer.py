from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:5].lower()
    found_palindromes = set()
    for combo in permutations(substring, 3):
        candidate = ''.join(combo)
        if candidate == candidate[::-1]:
            for length in range(4, 11):
                if length % 2 == 0:
                    extended_palindrome = candidate[:length // 2] + candidate[length // 2 - 1::-1]
                else:
                    extended_palindrome = candidate[:length // 2] + candidate[length // 2] + candidate[length // 2 - 1::-1]
                if extended_palindrome == extended_palindrome[::-1]:
                    found_palindromes.add(extended_palindrome)
    return found_palindromes