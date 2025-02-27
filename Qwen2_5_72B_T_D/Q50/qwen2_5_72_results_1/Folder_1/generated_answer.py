from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)
    words = [word.lower() for word in words if len(word) >= 3]
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                count += 1
                if count >= 96:
                    return True
    return False