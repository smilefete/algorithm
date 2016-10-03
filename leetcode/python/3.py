#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
'''
T
遍历字符串，用字典记录每个出现的字符（key:字符,value:索引），对于当前字符，查找是否在字典中出现过并且索引是否大于当前的开始索引，
如果满足说明这一步已经到了当前最大长度，更新最大长度，更新当前开始索引为字典中符合条件的索引值加1，更新字典中的字符索引，循环直到字符串末尾。
时间复杂度O(n)
'''
'''
耗时还是较多，原因在哪？
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        length=0
        begin=0
        for index,c in enumerate(s):
            if dic.has_key(c) and dic[c]>=begin:
                if index-begin>length:
                    length = index-begin
                begin = dic[c]+1
            dic[c]=index
        if len(s)-begin>length:
            length = len(s)-begin
        return length


if __name__ == '__main__':
    s=Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("bbbbb")
    print s.lengthOfLongestSubstring("pwwkew")





