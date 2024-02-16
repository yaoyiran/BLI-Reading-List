# Sample 1. Prompt Large Language Models (e.g., LLaMA) for BLI. Code grabbed from Prompt4BLI repo: "https://github.com/cambridgeltl/prompt4bli".
# This is the current state-of-the-art BLI approach.

from transformers import LlamaForCausalLM, LlamaTokenizer
tokenizer = LlamaTokenizer.from_pretrained("huggyllama/llama-7b",padding_side='left')
tokenizer.pad_token_id = tokenizer.eos_token_id
model = LlamaForCausalLM.from_pretrained("huggyllama/llama-7b").cuda()
model.eval()

TXT = ["The word 'you' in Chinese is 你. The word 'he' in Chinese is"]  # In-context learning: a '.' token will follow the target word. 

input_encs = tokenizer.batch_encode_plus(TXT,padding=True,add_special_tokens=True,return_tensors="pt")
max_len = 5 + input_encs.input_ids.size(1)
input_encs_cuda = {k:v.cuda() for k,v in input_encs.items()}
outputs = model.generate(**input_encs_cuda,num_beams=5, num_return_sequences=5,max_length=max_len,output_scores=True,return_dict_in_generate=True,do_sample=False)
output_sents = [tokenizer.decode(o, skip_special_tokens=True) for o in outputs.sequences]

target_word = output_sents[0].split(TXT[0])[1].split()[0].split(".")[0]

# Sample 2. Procrustes. Code grabbed from ContrastiveBLI repo: "https://github.com/cambridgeltl/ContrastiveBLI". Please refer to Appendix A.3 of paper "Improving Word Translation via Two-Stage Contrastive Learning".
# A representative mapping-based BLI approach.

import numpy as np
import torch

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






