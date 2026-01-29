import torch
import torch.nn.functional as f
def selfAttension(Q,K,V):
    dk = Q.size(-1)
    score = Q @ K.transpose(-2,-1) /dk**0.5

    scoreSIze = score.size(-1)
    mask = torch.triu(torch.ones(scoreSIze,scoreSIze), diagonal=1).bool()
    score = score.masked_fill(mask, float('-inf'))
    weight = f.softmax(score, dim=-1)

    return weight @ V, weight

inputVectors = torch.randn(1,4,8)
Q = K = V = inputVectors
result, weight = selfAttension(Q, K, V)
print("shape: ", result.shape)
print("Attention weight: ", weight)


