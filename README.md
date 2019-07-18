# cantonese-pos-tagger
Tagging written Cantonese with part-of-speech information, using the Stanford POS Tagger and the Hong Kong Cantonese Corpus.

Use the model

```python
from nltk.tag.stanford import StanfordPOSTagger
from nltk import word_tokenize
import nltk

stanford_model = 'stanford-postagger/models/cantonese.tagger'
stanford_jar = 'stanford-postagger/stanford-postagger.jar'
tagger = StanfordPOSTagger(stanford_model, stanford_jar)
tagger.java_options = '-mx4096m'
text = "some chinese segmented words"
print tagger.tag_sents(text)
```
