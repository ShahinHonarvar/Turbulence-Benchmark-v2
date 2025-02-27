from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        return sorted(s.lower())
    count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            count[count_chars(string)] += 1
    return sum((n * (n - 1) // 2 for n in count.values())) >= 115