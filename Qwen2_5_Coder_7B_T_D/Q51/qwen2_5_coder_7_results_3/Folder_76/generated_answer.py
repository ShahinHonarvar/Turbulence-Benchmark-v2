from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i].replace(' ', '').lower()
            word2 = words[j].replace(' ', '').lower()
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1) == Counter(word2)):
                anagram_count += 1
                if anagram_count > 91:
                    return False
    return True