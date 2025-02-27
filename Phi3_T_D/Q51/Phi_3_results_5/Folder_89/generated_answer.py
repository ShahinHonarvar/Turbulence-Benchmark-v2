from collections import defaultdict

def if_contains_anagrams(strings):

    def cmp(s1, s2):
        return ''.join(sorted(s1.lower())) == ''.join(sorted(s2.lower()))
    count = 0
    seen_anagrams = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            count += seen_anagrams[sorted_s]
            seen_anagrams[sorted_s] += 1
            if count > 73:
                return False
    return True