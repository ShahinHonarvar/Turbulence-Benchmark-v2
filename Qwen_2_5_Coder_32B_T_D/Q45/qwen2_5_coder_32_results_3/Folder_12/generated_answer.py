from collections import Counter
    import itertools

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if 'a' <= c <= 'z']
    count = Counter(letters)
    half_len = len(letters) // 2
    mid = ''
    if len(letters) % 2 == 1:
        for c in count:
            if count[c] % 2 == 1:
                mid = c
                count[c] -= 1
                break
        else:
            return set()
    half = []
    for c in count:
        half.extend(c * (count[c] // 2))
    half_palindromes = set((''.join(p) for p in itertools.permutations(half)))
    palindromes = {h + mid + h[::-1] for h in half_palindromes if len(h + mid + h[::-1]) >= 4}
    return palindromes