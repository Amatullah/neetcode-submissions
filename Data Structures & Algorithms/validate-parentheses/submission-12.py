class Solution:
    def isValid(self, s: str) -> bool:
        sc = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                sc.append(i)
            elif sc and ((i == ")" and sc[-1]== "(") or (i == "]" and sc[-1]== "[") or (i == "}" and sc[-1]== "{")):
                sc.pop()
            else:
                sc.append(i)
        return len(sc) == 0