from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(int)
    count = 0
    for word in words:
        word_sorted = ''.join(sorted(word.lower()))
        if len(word_sorted) >= 3:
            word_dict[word_sorted] += 1
            if word_dict[word_sorted] == 2:
                count += 1
            if count > 15:
                return False
    return True