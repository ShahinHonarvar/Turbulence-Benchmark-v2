import re
from collections import Counter

def if_contains_anagrams(input_list):
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            word1 = re.sub('[^a-zA-Z]', '', input_list[i]).lower()
            word2 = re.sub('[^a-zA-Z]', '', input_list[j]).lower()
            if len(word1) >= 3 and len(word2) >= 3 and (len(word1) == len(word2)) and (Counter(word1) == Counter(word2)):
                anagram_pairs += 1
                if anagram_pairs > 46:
                    return False
    return anagram_pairs <= 46