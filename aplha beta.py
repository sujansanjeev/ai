import math

def alpha_beta_pruning(curDepth, nodeIndex, alpha, beta, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        maxScore = float('-inf')
        for i in range(3):
            childIndex = nodeIndex * 3 + i
            if childIndex < len(scores):
                score = alpha_beta_pruning(curDepth + 1, childIndex, alpha, beta, False, scores, targetDepth)
                maxScore = max(maxScore, score)
                alpha = max(alpha, maxScore)
                if beta <= alpha:
                    break
        return maxScore
    else:
        minScore = float('inf')
        for i in range(3):
            childIndex = nodeIndex * 3 + i
            if childIndex < len(scores):
                score = alpha_beta_pruning(curDepth + 1, childIndex, alpha, beta, True, scores, targetDepth)
                minScore = min(minScore, score)
                beta = min(beta, minScore)
                if beta <= alpha:
                    break
        return minScore

# Driver code
scores = [3,4,5,5,10,4,3,1,4]

treeDepth = int(math.log(len(scores), 3))

print("The optimal value is:", alpha_beta_pruning(0, 0, float('-inf'), float('inf'), True, scores, treeDepth))
