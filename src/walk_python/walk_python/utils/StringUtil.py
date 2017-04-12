# -*- coding: UTF-8 -*-

'''
Created on 2017.4.3

@author: W.lu
'''

from BeautifulSoup import BeautifulSoup
from textrank4zh import TextRank4Sentence
import codecs

def escapeScript(sourceString):
    from __builtin__ import str
    soup = BeautifulSoup(sourceString)
    [s.extract() for s in soup('script')]
    #print 'soup result : %s' % str(soup)
    if soup:
        return str(soup)
    else:
        return ''
 
def genSummary(stringInfo):
    text = codecs.encode(stringInfo, 'gbk')
    tr4s = TextRank4Sentence(stop_words_file = 'D:/workspace/walk_python/src/walk_python/walk_python/utils/textrank4zh/stopwords.txt')
    tr4s.analyze(text,lower = True)
    s_list = tr4s.get_key_sentences(num=1,sentence_min_len=5)
    #print 'sumarry result : %s' % (s_list[0].sentence.encode('gbk'))
    if s_list[0].sentence:
        return s_list[0].sentence.encode('gbk')
    else:
        return ''


if __name__ == '__main__':
    sourceString = '''
    <script>a</script>
    baba
    <script>b</script>
    <h1>hi, world</h1>
    '''
    #string = genSummary(sourceString)
    string = escapeScript(sourceString)
    print(type(str(string)))    