from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    cnt = Counter(s)
    valid_chars = [c for c in cnt if c.isalpha() and cnt[c] >= 2]
    pals = set()
    for length in range(4, 9, 2):
        for perm in permutations(valid_chars, length // 2):
            half = ''.join(perm)
            if length % 2 == 0:
                full = half + half[::-1]
            else:
                for mid in valid_chars:
                    if cnt[mid] >= 3:
                        full = half + mid + half[::-1]
                        break
                else:
                    continue
            pals.add(full)
    return pals