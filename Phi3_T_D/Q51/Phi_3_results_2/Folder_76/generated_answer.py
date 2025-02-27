from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    count = defaultdict(int)
    valid_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                pair = tuple(sorted([strings[i].lower(), strings[j].lower()]))
                valid_pairs.add(pair)
    return len(valid_pairs) <= 91