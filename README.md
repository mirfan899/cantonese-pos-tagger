# cantonese-pos-tagger
Tagging written Cantonese with part-of-speech information, using the Stanford POS Tagger and the Hong Kong Cantonese Corpus.

Use the model

```python
from nltk.tag.stanford import StanfordPOSTagger

stanford_model = './cantonese.tagger'
stanford_jar = './stanford-postagger/stanford-postagger-3.9.1.jar'
tagger = StanfordPOSTagger(stanford_model, stanford_jar)
tagger.java_options = '-mx4096m'
text = [["我哋見到面之後買埋麥當勞早餐，就開車去野餐。"]]
print(tagger.tag_sents(text))
```
