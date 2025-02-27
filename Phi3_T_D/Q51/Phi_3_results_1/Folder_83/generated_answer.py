from collections import defaultdict

def if_contains_anagrams(lst):
    sorted_mapping = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        sorted_mapping[sorted_word].append(word)
    count = 0
    for words in sorted_mapping.values():
        if len(words) > 1 and len(words[0]) >= 3:
            count += len(words) * (len(words) - 1) // 2
            if count > 19:
                return False
    return True