import re

def word_frequency(sentence):
    word_dict = {}
    words = re.findall(r'\w+', sentence.lower())
    
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
