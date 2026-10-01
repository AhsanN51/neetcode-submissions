class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk1=[]
        val=0
        for i in tokens:
            #print("st ",stk1)
            if i.lstrip("-").isdigit() and int(i)>=-200 and int(i)<=200:
                stk1.append(str(i))
            else: 
                b,a=int(stk1.pop()),int(stk1.pop())
                if i=='+':
                    val=a+b
                elif i=='*':
                    val=a*b
                elif i=='/':
                    val=a/b
                else:
                    val=a-b
                stk1.append(val)
            #print("ed ",stk1)
        return int(stk1[-1])