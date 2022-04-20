# Bilingual Lexicon Induction Reading List
This is a reading list for Bilingual Lexicon Induction (BLI), also known as Word Translation, Bilingual Lexicon Extraction, Bilingual Dictionary Induction, and so forth, closely related to the topic of Cross-Lingual Word Embeddings (CLWEs). The list mainly includes 2018-2022 publications. ***Frequently updated. Pull requests and discussions are welcome!***

# Most Frequently Used Baselines
### 1. Procrustes

**Normalized Word Embedding and Orthogonal Transform for Bilingual Word Translation (NAACL 2015).**<br>
*Chao Xing, Dong Wang, Chao Liu, Yiye Lin*<br>
[[paper]](https://aclanthology.org/N15-1104.pdf)

**Comments:** Beginners could also refer to [Procrustes on Wikipedia](https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem) and our sample code [./SampleCode.py](https://github.com/yaoyiran/Awesome-Bilingual-Lexicon-Induction-Papers-2022/blob/main/SampleCode.py). 

### 2. MUSE

**Word Translation Without Parallel Data (ICLR 2018).**<br>
*Guillaume Lample, Alexis Conneau, Marc'Aurelio Ranzato, Ludovic Denoyer, Hervé Jégou*<br>
[[Paper]](https://openreview.net/pdf?id=H196sainb)
[[Code]](https://github.com/facebookresearch/MUSE)

### 3. RCSLS

**Loss in Translation: Learning Bilingual Word Mapping with a Retrieval Criterion (EMNLP 2018).**<br>
*Armand Joulin, Piotr Bojanowski, Tomas Mikolov, Hervé Jégou, Edouard Grave*<br>
[[paper]](https://aclanthology.org/N15-1104.pdf)
[[Code]](https://github.com/facebookresearch/fastText/tree/main/alignment)

### 4. VecMap

**A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings (ACL 2018).**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre*<br>
[[paper]](https://aclanthology.org/P18-1073/)
[[Code]](https://github.com/artetxem/vecmap)

**Generalizing and Improving Bilingual Word Embedding Mappings with a Multi-Step Framework of Linear Transformations (AAAI 2018).**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre*<br>
[[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/11992)
[[Code]](https://github.com/artetxem/vecmap)

**Comments:** VecMap supports unsupervised (its ACL 2018 paper), semi-supervised and supervised (its AAAI 2018 paper) BLI settings.

# Recent Progress in BLI: Methodologies

### 1. ContrastiveBLI

**Improving Word Translation via Two-Stage Contrastive Learning (ACL 2022).**<br>
*Yaoyiran Li, Fangyu Liu, Nigel Collier, Anna Korhonen, Ivan Vulić*<br>
[[paper]](https://arxiv.org/abs/2203.08307)
[[Code]](https://github.com/cambridgeltl/ContrastiveBLI)

**Comments:** New (2022) state-of-the-art method for semi-supervised and supervised BLI!

### 2. BLISS

**Bilingual Lexicon Induction with Semi-supervision in Non-Isometric Embedding Spaces (ACL 2019).**<br>
*Barun Patra, Joel Ruben Antony Moniz, Sarthak Garg, Matthew R. Gormley, Graham Neubig*<br>
[[paper]](https://aclanthology.org/P19-1018/)
[[Code]](https://github.com/joelmoniz/BLISS)

### 3. GeoMM

**Learning Multilingual Word Embeddings in Latent Metric Space: A Geometric Approach (TACL 2019).**<br>
*Pratik Jawanpuria, Arjun Balgovind, Anoop Kunchukuttan, Bamdev Mishra*<br>
[[paper]](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00257/43509/Learning-Multilingual-Word-Embeddings-in-Latent)
[[Code]](https://github.com/anoopkunchukuttan/geomm)

### 4. LNMap

**LNMap: Departures from Isomorphic Assumption in Bilingual Lexicon Induction Through Non-Linear Mapping in Latent Space (EMNLP 2020).**<br>
*Tasnim Mohiuddin, M Saiful Bari, Shafiq Joty*<br>
[[paper]](https://aclanthology.org/2020.emnlp-main.215/)
[[Code]](https://github.com/taasnim/lnmap)

### 5. InstaMap

**Non-Linear Instance-Based Cross-Lingual Mapping for Non-Isomorphic Embedding Spaces (ACL 2020).**<br>
*Goran Glavaš, Ivan Vulić*<br>
[[paper]](https://aclanthology.org/2020.acl-main.675/)
[[Code]](https://github.com/codogogo/instamap)

### 6. CSCBLI

**Combining Static Word Embeddings and Contextual Representations for Bilingual Lexicon Induction (Findings of ACL 2021).**<br>
*Jinpeng Zhang, Baijun Ji, Nini Xiao, Xiangyu Duan, Min Zhang, Yangbin Shi, Weihua Luo*<br>
[[paper]](https://aclanthology.org/2021.findings-acl.260/)
[[Code]](https://github.com/zjpbinary/CSCBLI)

### 7. mBERT

**It’s not Greek to mBERT: Inducing Word-Level Translations from Multilingual BERT (BlackboxNLP Workshop 2020).**<br>
*Hila Gonen, Shauli Ravfogel, Yanai Elazar, Yoav Goldberg*<br>
[[paper]](https://aclanthology.org/2020.blackboxnlp-1.5/)
[[Code]](https://github.com/gonenhila/mbert)

### 8. IterNorm

**Are Girls Neko or Shōjo? Cross-Lingual Alignment of Non-Isomorphic Embeddings with Iterative Normalization (ACL 2019).**<br>
*Mozhi Zhang, Keyulu Xu, Ken-ichi Kawarabayashi, Stefanie Jegelka, Jordan Boyd-Graber*<br>
[[paper]](https://aclanthology.org/P19-1307.pdf)
[[Code]](https://github.com/zhangmozhi/iternorm)

### 9. SpecNorm

**Normalization of Language Embeddings for Cross-Lingual Alignment (ICLR 2022).**<br>
*Prince Osei Aboaggye, Yan Zheng, Junpeng Wang, Michael Yeh, Wei Zhang, Liang Wang, Hao Yang, Jeff M. Phillips*<br>
[[paper]](https://openreview.net/pdf?id=Nh7CtbyoqV5)
[[Code]](https://github.com/poaboagye/SpecNorm)

### 10. JointAlign

**Cross-lingual Alignment vs Joint Training: A Comparative Study and A Simple Unified Framework (ICLR 2020).**<br>
*Zirui Wang<sup>+</sup>, Jiateng Xie<sup>+</sup>, Ruochen Xu, Yiming Yang, Graham Neubig, Jaime Carbonell (+: equal contribution)*<br>
[[paper]](https://arxiv.org/abs/1910.04708)
[[Code]](https://github.com/thespectrewithin/joint_align)

### 11. FIPP

**Filtered Inner Product Projection for Crosslingual Embedding Alignment (ICLR 2021).**<br>
*Vin Sachidananda, Ziyi Yang, Chenguang Zhu*<br>
[[paper]](https://openreview.net/pdf?id=A2gNouoXE7)
[[Code]](https://github.com/vinsachi/FIPPCLE)

### 12. ClassyMap

**Classification-Based Self-Learning for Weakly Supervised Bilingual Lexicon Induction (ACL 2020).**<br>
*Mladen Karan, Ivan Vulić, Anna Korhonen, Goran Glavaš*<br>
[[paper]](https://aclanthology.org/2020.acl-main.618/)
[[Code]](https://github.com/mladenk42/ClassyMap)

### 13. MUVE

**Visual Grounding in Video for Unsupervised Word Translation (CVPR 2020).**<br>
*Gunnar A. Sigurdsson, Jean-Baptiste Alayrac, Aida Nematzadeh, Lucas Smaira, Mateusz Malinowski, Joao Carreira, Phil Blunsom, Andrew Zisserman*<br>
[[paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Sigurdsson_Visual_Grounding_in_Video_for_Unsupervised_Word_Translation_CVPR_2020_paper.html)
[[Code]](https://github.com/gsig/visual-grounding)

### 14. Bidirectional-RMP

**A Relaxed Matching Procedure for Unsupervised BLI (ACL 2020).**<br>
*Xu Zhao, Zihao Wang, Yong Zhang, Hao Wu*<br>
[[paper]](https://aclanthology.org/2020.acl-main.274/)
[[Code]](https://github.com/BestActionNow/bidirectional-RMP)

### 15. (Methodology)

**A Graph-based Coarse-to-fine Method for Unsupervised Bilingual Lexicon Induction (ACL 2020).**<br>
*Shuo Ren, Shujie Liu, Ming Zhou, Shuai Ma*<br>
[[paper]](https://aclanthology.org/2020.acl-main.318/)

### 16. CrossLingualELMo

**Cross-Lingual Alignment of Contextual Word Embeddings, with Applications to Zero-shot Dependency Parsing (NAACL 2019).**<br>
*Tal Schuster, Ori Ram, Regina Barzilay, Amir Globerson*<br>
[[paper]](https://aclanthology.org/N19-1162/)
[[Code]](https://github.com/TalSchuster/CrossLingualContextualEmb)

### 17. (Methodology)

**Multilingual Alignment of Contextual Word Representations (ICLR 2020).**<br>
*Steven Cao, Nikita Kitaev, Dan Klein*<br>
[[paper]](https://openreview.net/forum?id=r1xCMyBtPS)

### 18. Bitext-Lexind

**Bilingual Lexicon Induction via Unsupervised Bitext Construction and Word Alignment (ACL 2021).**<br>
*Haoyue Shi, Luke Zettlemoyer, Sida I. Wang*<br>
[[paper]](https://aclanthology.org/2021.acl-long.67/)
[[Code]](https://github.com/facebookresearch/bitext-lexind)

### 19. Monoses

**Bilingual Lexicon Induction through Unsupervised Machine Translation (ACL 2019).**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre*<br>
[[paper]](https://aclanthology.org/P19-1494/)
[[Code]](https://github.com/artetxem/monoses)

### 20. (Methodology)

**Unsupervised Alignment of Embeddings with Wasserstein Procrustes (AISTATS 2019).**<br>
*Edouard Grave, Armand Joulin, Quentin Berthet*<br>
[[paper]](http://proceedings.mlr.press/v89/grave19a.html)
[[Code]](https://github.com/facebookresearch/fastText/tree/main/alignment)

### 21. OTAlign

**Gromov-Wasserstein Alignment of Word Embedding Spaces (EMNLP 2018).**<br>
*David Alvarez-Melis, Tommi Jaakkola*<br>
[[paper]](https://aclanthology.org/D18-1214/)
[[Code]](https://github.com/dmelis/otalign)

### 22. L1-Refinement

**Cross-Lingual Word Embedding Refinement by ℓ1 Norm Optimisation (NAACL 2021).**<br>
*Xutan Peng, Chenghua Lin, Mark Stevenson*<br>
[[paper]](https://aclanthology.org/2021.naacl-main.214/)
[[Code]](https://github.com/Pzoom522/L1-Refinement)

### 23. (Methodology)

**A Simple and Effective Approach to Robust Unsupervised Bilingual Dictionary Induction (COLING 2020).**<br>
*Yanyang Li, Yingfeng Luo, Ye Lin, Quan Du, Huizhen Wang, Shujian Huang, Tong Xiao, Jingbo Zhu*<br>
[[paper]](https://aclanthology.org/2020.coling-main.526/)


### 24. ContextualMapping

**Cross-Lingual BERT Contextual Embedding Space Mapping with Isotropic and Isometric Conditions (Preprint 2021).**<br>
*Haoran Xu, Philipp Koehn*<br>
[[paper]](https://arxiv.org/pdf/2107.09186.pdf)
[[Code]](https://github.com/fe1ixxu/Contextual_Mapping)

# Recent Progress in BLI: Datasets, Benchmarks, Analyses & Surveys
### 1. XLING (Dataset)

**How to (Properly) Evaluate Cross-Lingual Word Embeddings: On Strong Baselines, Comparative Analyses, and Some Misconceptions (ACL 2019).**<br>
*Goran Glavaš, Robert Litschko, Sebastian Ruder, Ivan Vulić*<br>
[[paper]](https://aclanthology.org/P19-1070/)
[[Code]](https://github.com/codogogo/xling-eval)

### 2. Panlex-BLI (Dataset)

**Do We Really Need Fully Unsupervised Cross-Lingual Embeddings? (EMNLP 2019).**<br>
*Ivan Vulić, Goran Glavaš, Roi Reichart, Anna Korhonen*<br>
[[paper]](https://aclanthology.org/D19-1449/)
[[Code]](https://github.com/cambridgeltl/panlex-bli)

### 3. (Analysis)
**On the Limitations of Unsupervised Bilingual Dictionary Induction (ACL 2018).**<br>
*Anders Søgaard, Sebastian Ruder, Ivan Vulić*<br>
[[paper]](https://aclanthology.org/P18-1072/)

### 4. ISO-Study

**Are All Good Word Vector Spaces Isomorphic? (EMNLP 2020).**<br>
*Ivan Vulić, Sebastian Ruder, Anders Søgaard*<br>
[[paper]](https://aclanthology.org/2020.emnlp-main.257/)
[[Code]](https://github.com/cambridgeltl/iso-study)

### 5. (Survey)

**A Survey of Cross-Lingual Word Embedding Models (JAIR 2019).**<br>
*Sebastian Ruder, Ivan Vulić, Anders Søgaard*<br>
[[paper]](https://www.jair.org/index.php/jair/article/view/11640)


### 6. Embeddings (Dataset)

**Should All Cross-Lingual Embeddings Speak English? (ACL 2020).**<br>
*Antonios Anastasopoulos, Graham Neubig*<br>
[[paper]](https://aclanthology.org/2020.acl-main.766/)
[[Code]](https://github.com/antonisa/embeddings)

# Pull Requests Are Welcome:

### No.

** ().**<br>
**<br>
[[paper]]()
[[Code]]()

**Comments:**

### No.

** ().**<br>
**<br>
[[paper]]()
[[Code]]()

**Comments:**
