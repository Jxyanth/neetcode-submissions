class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def operation(a , b , sym):
            if(sym == "+"):
                return a + b
            elif(sym == "-"):
                return a - b
            elif(sym == "*"):
                return a*b
            else:
                return int(a/b)
        for i in tokens:
            if i in "+-/*":
                b = stack.pop()
                a = stack.pop()
                res = int(operation(a,b,i))
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]


