import re

def filter_chars(s):
    pattern = re.compile('[^18:95]K-a]')
    return pattern.sub('', s)