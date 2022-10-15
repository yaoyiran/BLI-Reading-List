import numpy as np
import torch

# Procrustes. Grabed from ContrastiveBLI repo: "https://github.com/cambridgeltl/ContrastiveBLI". Please refer to Appendix A.3 of paper "Improving Word Translation via Two-Stage Contrastive Learning".

def procrustes(X_src, Y_tgt):
    # X_src: source WEs of size (n, d1), np.array 
    # Y_tgt: target WEs of size (n, d2), np.array
    # n: number of word translation pairs for training
    # d1 and d2: dimension of WEs. d1<=d2 (usually d1=d2), typically 300 for fastText WEs and 768 for mBERT WEs.
    X_dim = X_src.shape[1]
    Y_dim = Y_tgt.shape[1]
    U, s, V = np.linalg.svd(np.dot(X_src.T, Y_tgt))
    if X_dim == Y_dim:
        return np.dot(U, V)
    elif X_dim < Y_dim:
        zeros_pad = np.zeros([X_dim,Y_dim-X_dim])
        U = np.concatenate((U,zeros_pad),axis=1)
        return np.dot(U, V)
    else:
        zeros_pad = np.zeros([X_dim-Y_dim, Y_dim])
        V = np.concatenate((V,zeros_pad),axis=0)
        return np.dot(U, V)

# Require: X_src of size (n, dim_X), Y_tgt of size (n, dim_Y), torch.tensor
# Output: X_src_mapped, torch.tensor
linear_weights = procrustes(X_src.numpy(), Y_tgt.numpy())
linear_weights = torch.tensor(linear_weights,dtype=torch.float32)

linear_layer = torch.nn.Linear(dim_X,dim_Y,bias=False)
linear_layer.weight.data = linear_weights.t()
linear_layer.requires_grad_(False)

X_src_mapped = linear_layer(X_src)
