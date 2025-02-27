from collections import defaultdict
import itertools

def create_normalized_key(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_keys = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        normalized_key = create_normalized_key(string)
        normalized_keys[normalized_key].append(string)
    for strings_with_same_normalized_key in normalized_keys.values():
        if len(strings_with_same_normalized_key) > 1:
            combinations_to_check = list(itertools.combinations(strings_with_same_normalized_key, 2))
            for pair in combinations_to_check:
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True