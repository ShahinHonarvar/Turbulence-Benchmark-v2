from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = 0
    normalized_words = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            count += normalized_words[normalized]
            normalized_words[normalized] += 1
    return count >= 96