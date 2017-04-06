# -*- coding: UTF-8 -*-

'''
Created on 2017年4月3日

@author: 01158130
'''

from BeautifulSoup import BeautifulSoup

def escapeScript(sourceString):
    soup = BeautifulSoup(sourceString)
    [s.extract() for s in soup('script')]
    print soup
    return soup
    
if __name__ == '__main__':
    sourceString = '''
    <script>a</script>
    baba
    <script>b</script>
    <h1>hi, world</h1>
    '''
    escapeScript(sourceString)    