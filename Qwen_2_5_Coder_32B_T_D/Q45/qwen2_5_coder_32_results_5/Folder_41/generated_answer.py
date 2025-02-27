from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:4])).lower()
    if len(letters) < 2:
        return set()
    p = {''.join(x) for x in permutations(letters, 2)}
    palindromes = {f'{x}{y}{x}' for x in p for y in 'abcdefghijklmnopqrstuvwxyz'}
    return palindromes.intersection({s.lower() for s in permutations(''.join(sorted(letters) * 3), 3)})