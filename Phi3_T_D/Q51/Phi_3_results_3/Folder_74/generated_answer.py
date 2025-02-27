from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)

    def get_key(s):
        return ''.join(sorted(s.lower()))
    for word in words:
        if len(word) >= 3:
            count[get_key(word)] += 1
    anagram_pairs = sum([v * (v - 1) // 2 for k, v in count.items()])
    return anagram_pairs <= 57