# -*- coding: utf-8 -*-
from pythainlp import word_tokenize
from pythainlp.word_vector import thai2vec
model=thai2vec.get_model()
def sentence_similarity(s1,s2):
    return model.wmdistance(' '.join(word_tokenize(s1)), ' '.join(word_tokenize(s2)))
sentences = [
    "ผมเป็นนักศึกษา",
    "นักศึกษาคือผม"
]
 
focus_sentence = "ผมเป็นนักศึกษา"
 
for sentence in sentences:
    print ("Similarity(\"%s\", \"%s\") = %.3f" % (focus_sentence, sentence, sentence_similarity(focus_sentence, sentence)))