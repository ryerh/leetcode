import unittest


class Solution:
    def __init__(self):
        self.answer_depth = 0

    def is_match(self, w1, w2):
        mismatch_counter = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                mismatch_counter += 1
        return mismatch_counter == 1

    def get_answer(self, answers, word_list, final_answers):
        min = 0
        max = len(word_list)
        for l in answers:
            if len(l) <= max:
                min = len(l)
        for l in answers:
            if len(l) == min:
                final_answers.append(l)

    def find_path(self, begin, end, word_list, stack, answers, depth):
        if not (end in word_list):
            return

        if self.is_match(begin, end):
            stack += [end]
            answers.append(stack)
            return

        for i, w in enumerate(word_list):
            if (w not in stack) and self.is_match(w, begin):
                if self.is_match(w, end):
                    answer = stack + [w, end]
                    answers.append(answer)
                    self.answer_depth = depth
                elif self.answer_depth == 0 or depth + 1 <= self.answer_depth:
                    next_stack = stack + [w]
                    next_word_list = word_list[0:i] + word_list[i+1:]
                    self.find_path(w, end, next_word_list, next_stack, answers, depth + 1)

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        stack = [beginWord]
        answers = []
        final_answers = []
        self.find_path(beginWord, endWord, wordList, stack, answers, 0)
        print('answers', len(answers), answers)
        self.get_answer(answers, wordList, final_answers)
        return final_answers


class TestSolution(unittest.TestCase):

#   def test_1(self):
#       print(Solution().findLadders(
#           'hot',
#           'dog',
#           []
#       ))

#   def test_2(self):
#       print(Solution().findLadders(
#           'a',
#           'c',
#           ['a', 'b', 'c']
#       ))

#   def test_3(self):
#       print(Solution().findLadders(
#           'hot',
#           'dog',
#           ["hot","cog","dog","tot","hog","hop","pot","dot"]
#       ))

#   def test_4(self):
#       exptected_answer = [
#           ["kiss","diss","disk","dusk","tusk"],
#           ["kiss","miss","muss","musk","tusk"]
#       ]
#       my_answer = Solution().findLadders(
#           "kiss",
#           "tusk",
#           [
#               "miss","dusk","kiss","musk","tusk",
#               "diss","disk","sang","ties","muss"
#           ]
#       )
#       print(my_answer)
#       # self.assertListEqual(exptected_answer, my_answer, 'wrong_answer')

#   def test_5(self):
#       my_answer = Solution().findLadders(
#           "hot",
#           "dog",
#           ["hot","dog","dot"]
#       )

    def test_6(self):
        my_answer = Solution().findLadders(
            "qa",
            "sq",
            ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
        )
        print('my_answer', len(my_answer), my_answer)

#   def test_7(self):
#       my_answer = Solution().findLadders(
#           "leet",
#           "code",
#           ["lest","leet","lose","code","lode","robe","lost"]
#       )
#       print(my_answer)


if __name__ == '__main__':
    unittest.main()

