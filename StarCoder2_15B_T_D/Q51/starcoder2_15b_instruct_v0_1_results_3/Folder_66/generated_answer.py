import re

def if_contains_anagrams(strings):
    anagrams = []
    for i, string in enumerate(strings):
        string = re.sub('[^a-zA-Z]', '', string).lower()
        if len(string) >= 3:
            for j in range(i + 1, len(strings)):
                other_string = re.sub('[^a-zA-Z]', '', strings[j]).lower()
                if len(other_string) >= 3 and sorted(string) == sorted(other_string):
                    anagrams.append((string, other_string))
    if len(anagrams) <= 64:
        return True
    else:
        return False