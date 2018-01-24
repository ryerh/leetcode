# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        num = ''
        stack = []
        for c in s:
            if (c == ' '):
                continue
            elif (c == '(' or c == ')' or c == '+' or c == '-'):
                if (num != ''):
                    stack.append(int(num))
                    num = ''
                stack.append(c)
            else:
                num += c
        if num != '':
            stack.append(int(num))

        stack = list(reversed(stack))

        stack2 = []
        for t in stack:
            if t == '(':
                while (stack2[-2] != ')'):
                    ln = stack2.pop()
                    op = stack2.pop()
                    rn = stack2.pop()
                    if op == '+':
                        r = ln + rn
                    else:
                        r = ln - rn
                    stack2.append(r)
                n = stack2.pop()
                lp = stack2.pop()
                stack2.append(n)
            else:
                stack2.append(t)

        while len(stack2) > 1:
            ln = stack2.pop()
            op = stack2.pop()
            rn = stack2.pop()
            if op == '+':
                r = ln + rn
            else:
                r = ln - rn
            stack2.append(r)

        return stack2[0]
