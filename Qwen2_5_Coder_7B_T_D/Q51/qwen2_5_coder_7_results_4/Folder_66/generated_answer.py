from collections import defaultdict

def if_contains_anagrams(words):
    word_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_count[sorted_word] += 1
            if word_count[sorted_word] > 2:
                return False
    return True