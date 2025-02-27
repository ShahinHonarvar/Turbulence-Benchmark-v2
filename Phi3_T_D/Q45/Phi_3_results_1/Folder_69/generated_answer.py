from itertools import permutations

def palindromes_between_indices(s):
    start, end = (0, 3)
    letters = [ch.lower() for ch in s[start:end + 1] if ch.isalpha()]
    letters.sort()
    palindromes = {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)}
    valid_palindromes = {p[:len(p) // 2] + p[:len(p) // 2][::-1] for p in palindromes if p[:len(p) // 2] == p[:len(p) // 2][::-1]}
    return valid_palindromes