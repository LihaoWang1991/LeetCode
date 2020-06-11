# problem link: https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # pre-processiong，construct adjacency list of words to reduce computation later
        adj_dict = {}
        for word_i in wordList:
            for j in range(len(word_i)):
                word_type = word_i[0:j] + "*" + word_i[j+1:]
                if word_type not in adj_dict:
                    adj_dict[word_type] = [word_i]
                else:
                    adj_dict[word_type].append(word_i)
        
        queue = [beginWord]
        ans = 1
        while queue != []:
            for i in range(len(queue)):
                word_i = queue.pop(0)
                if word_i == endWord:
                    return ans
                for j in range(len(word_i)):
                    word_type = word_i[0:j] + "*" + word_i[j+1:]
                    if word_type in adj_dict:
                        queue += adj_dict[word_type]
                        del adj_dict[word_type]