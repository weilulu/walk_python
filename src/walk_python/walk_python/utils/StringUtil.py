# -*- coding: UTF-8 -*-

'''
Created on 2017年4月3日

@author: W.lu
'''

from BeautifulSoup import BeautifulSoup
from textrank4zh import TextRank4Sentence
import codecs

def escapeScript(sourceString):
    soup = BeautifulSoup(sourceString)
    [s.extract() for s in soup('script')]
    #print soup
    return soup
 
def genSummary(stringInfo):
    text = codecs.encode(stringInfo, 'gbk')
    print text
    tr4s = TextRank4Sentence(stop_words_file = 'D:/Workspaces/walk_python/src/walk_python/walk_python/utils/textrank4zh/stopwords.txt')
    tr4s.analyze(text,lower = True)
    s_list = tr4s.get_key_sentences(num=1,sentence_min_len=5)
    #print s_list[0].sentence
    return s_list[0].sentence;
if __name__ == '__main__':
    sourceString = '''
    <script>a</script>
    baba
    <script>b</script>
    <h1>hi, world</h1>
    '''
    genSummary(escapeScript(sourceString))    