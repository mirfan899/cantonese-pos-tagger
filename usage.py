from nltk.tag.stanford import StanfordPOSTagger

stanford_model = './cantonese.tagger'
stanford_jar = './stanford-postagger/stanford-postagger-3.9.1.jar'
tagger = StanfordPOSTagger(stanford_model, stanford_jar)
tagger.java_options = '-mx4096m'
text = [["一四八"]]
print(tagger.tag_sents(text))