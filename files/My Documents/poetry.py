# -*- coding: utf-8 -*-
"""
Poetry

Created on Tue Oct  9 16:47:11 2018

@author: p122506
"""
import random

intros = ["when", "although", "after", "before", "because", "yesterday,", 
          "last week,"]
articles = ["the", "a", "another", "no", "this", "that"]
subjects = ["man", "woman", "boy", "girl", "cat", "dog", "child", "horse"]
adjectives = ["beautiful", "horrible", "nice", "large", "tall", "tiny", "good",
              "bad", "small", "hot", "cold", "terrible", "disgusting", ""]
verbs = ["sang", "jumped", "ran", "looked", "cried", "slept", "awoke", 
         "played", "yelled", "fell"]
adverbs = ["solemnly", "loudly", "quitely", "well", "badly", "urgently", ""]

lines = int(input("How many lines? "))
print()
for i in range(lines):
    print(random.choice(intros), random.choice(articles), 
          random.choice(subjects), random.choice(verbs), 
          random.choice(adverbs))

