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
    text = codecs.encode(stringInfo, 'utf-8')
    tr4s = TextRank4Sentence(stop_words_file = 'D:/workspace/walk_python/src/walk_python/walk_python/utils/textrank4zh/stopwords.txt')
    tr4s.analyze(text,lower = True)
    s_list = tr4s.get_key_sentences(num=1,sentence_min_len=5)
    #print 'sumarry result : %s' % (s_list[0].sentence.encode('gbk'))
    if s_list[0].sentence:
        return s_list[0].sentence.encode('utf-8', 'ignore')
    else:
        return ''


if __name__ == '__main__':
    sourceString = '''
    燕燕于飞，差池其羽。之子于归，远送于野。瞻望弗及，泣涕如雨。

燕燕于飞，颉之颃之。之子于归，远于将之。瞻望弗及，伫立以泣。

燕燕于飞，下上其音。之子于归，远送于南。瞻望弗及，实劳我心。

仲氏任只，其心塞渊。终温且惠，淑慎其身。先君之思，以勖寡人。
    '''
    string = genSummary(sourceString)
    print(string)
    #string = escapeScript(sourceString)
    #print(type(str(string)))    