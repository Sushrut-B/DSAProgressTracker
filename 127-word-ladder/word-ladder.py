class Solution(object):
    def ladderLength(self, startWord, targetWord, wordList):
        words=set(wordList)
        if targetWord not in words:
            return 0
        
        q=deque()
        q.append((startWord,1))
        words.discard(startWord)

        while q:
            word,steps=q.popleft()
            if word == targetWord:
                return steps
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord=word[:i] + char + word[i+1:]
                    if newWord in words:
                        words.remove(newWord)
                        q.append((newWord,steps+1))
        return 0
    
