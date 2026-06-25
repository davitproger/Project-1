from fuzzywuzzy import fuzz

def string_distance (strings, target):
    result={}

    for word in strings:
        result[word]=fuzz.ratio(word, target)
    return result
