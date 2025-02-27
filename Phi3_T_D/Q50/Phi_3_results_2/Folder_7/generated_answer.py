from collections import defaultdict

def if_contains_anagrams(strings):

    def build_signature(s):
        return ''.join(sorted(s.lower()))
    count = 0
    signatures = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sig = build_signature(s)
        count += signatures[sig]
        signatures[sig] += 1
    return count >= 178