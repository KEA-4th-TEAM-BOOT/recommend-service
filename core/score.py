import torch

def cal_score(a, b):
    '''
    코사인 유사도 구하는 함수
    '''
    if len(a.shape) == 1: a = a.unsqueeze(0)
    if len(b.shape) == 1: b = b.unsqueeze(0)

    a_norm = a / a.norm(dim=1)[:, None]
    b_norm = b / b.norm(dim=1)[:, None]

    return torch.mm(a_norm, b_norm.transpose(0, 1)) * 100

def show_embedding_score(emb1, emb2):

    embeddings_0 = torch.Tensor(emb1)
    embeddings_1 = torch.Tensor(emb2)

    score = cal_score(embeddings_0, embeddings_1)

    return score