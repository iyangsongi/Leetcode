class Solution:
    '''
    思路：按照空格分隔句子单词，对单词进行反转，然后空格拼接
    '''
    def reverseWords(self, s: str) -> str:
         return ' '.join(i[::-1] for i in s.split())
        