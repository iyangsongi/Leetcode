class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if strs:
            i=1
            while True:
                sliced=strs[0][:i]
                for str in strs:
                    if sliced!=str[:i]:return sliced[:i-1]
                i+=1
        else:
            return ""