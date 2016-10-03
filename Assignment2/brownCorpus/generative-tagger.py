#import nltk and the corpus
import nltk
from nltk.corpus import brown

print "_______________________imported corpus_____________________________"
brown_tagged_sents = brown.tagged_sents()
brown_sents = brown.sents()

size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t2.evaluate(test_sents)