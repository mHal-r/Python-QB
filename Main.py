
from StanfordCoreNLP import StanfordCoreNLP
import re, collections
#from lxml import etree
from ArticleMap import ArticleMap
import xml.etree.ElementTree as ET
ET.register_namespace("", "http://www.mediawiki.org/xml/export-0.10/")
tree = ET.parse("TestData.xml")
root = tree.getroot()
articles = ET.parse("Wikipedia-Physics-Articles.xml")
test_question = []
test_answer = []
test_output = []
article_data = {}
article_clean = {}  #title and then an article map
aroot = articles.getroot()
pipeline = StanfordCoreNLP()
def main():

    for q in root.iter("question"):
        data = q.text
        test_question.append(data)
    for a in root.iter("answer"):
        test_answer.append(a)
    for o in root.iter("output"):
        test_output.append(o)
      #  print(data)
  #  print(ET.tostring(aroot, encoding='utf8').decode('utf8'))
    for p in aroot.iter("{http://www.mediawiki.org/xml/export-0.10/}page"):
        for i in p.iter():
            if(i.tag == "{http://www.mediawiki.org/xml/export-0.10/}title" ):
                title = i.text
            if(i.tag == "{http://www.mediawiki.org/xml/export-0.10/}text" ):
                article = i.text
        article[title] = article
    for i in article:
        article_clean[i] = cleanData(article[i])
def cleanData(text):
    words = set()
    doc = pipeline.annotate(text)
    for sentence in doc["sentences"]:
        # Get the OpenIE triples for the sentence
        # countOf function for sets
        triples = sentence["openie"]
        for triple in triples:
            noun1 = triple.subjectLemmaGloss();
            noun2 = triple.objectLemmaGloss();
            words.add(noun1)
            words.add(noun2)
    return words
def analyzeText(keyword, tryword):
    score = 0
    n1 = 0
    n2 = 0
    n3 = 0
    N = article_clean.__sizeof__()
    for entry in article_clean.values():
        if (keyword in entry) :
            freq = calcFrequency(entry, keyword) # this is me trying to produce a score weighted with frequency
            n1 += freq
        if (tryword in entry):
            freq = calcFrequency(entry, tryword)
            n3 += freq
        elif(tryword in entry):
            freq = calcFrequency(entry, tryword)
            n2 += freq
            score = n3/N
        liftscore = n3 / n2; # if its zero it's vv bad
        # liftscore is to check how relevant the keyword is among articles that have the tryword
        score *= liftscore
        return score
def calcFrequency(text, keyword):
    raw = text.countOf(keyword)
    max = 0
    for i in text :
        max = max(text.countOf(i), max)
    return raw/max
if __name__=="__main__":
        main()

