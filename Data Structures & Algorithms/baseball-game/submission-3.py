class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = [0]
        for i in range(len(operations)):
            wysokosc = len(scores)-1
            if operations[i] == '+':
                scores.append(scores[wysokosc] + scores[wysokosc - 1])
            elif operations[i] == 'D':
                scores.append(scores[wysokosc]*2)
            elif operations[i] == 'C':
                scores.pop()
            elif operations[i] != 'C':
                scores.append(int(operations[i]))
            print(scores)
        return sum(scores)