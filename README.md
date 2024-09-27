# Bilingual Lexicon Induction Reading List
This is a reading list for Bilingual Lexicon Induction (BLI), also known as Word Translation, Bilingual Lexicon Extraction, Bilingual Dictionary Induction, and so forth. A large body of BLI work relies on calculating Cross-Lingual Word Embeddings (CLWEs) for word retrieval; some other BLI approaches learn a pairwise classifier for BLI; recent work prompts large language models for BLI and achieves new state-of-the-art BLI performance. The list mainly includes 2018-2024 publications. ***Frequently updated. Pull requests and discussions are welcome!***

# Classical Methods (Before 2019)

### 1. Translation Matrix

**Exploiting Similarities among Languages for Machine Translation (arXiv 2013)**<br>
*Tomas Mikolov, Quoc V. Le, Ilya Sutskever*<br>
[[Paper]](https://arxiv.org/pdf/1309.4168)

### 2. Procrustes

**Normalized Word Embedding and Orthogonal Transform for Bilingual Word Translation (NAACL 2015)**<br>
*Chao Xing, Dong Wang, Chao Liu, Yiye Lin*<br>
[[Paper]](https://aclanthology.org/N15-1104.pdf)

**Comments:** Beginners could also refer to [Procrustes on Wikipedia](https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem) and our sample code [./SampleCode.py](https://github.com/yaoyiran/Awesome-Bilingual-Lexicon-Induction-Papers-2022/blob/main/SampleCode.py). 

### 3. MUSE

**Word Translation Without Parallel Data (ICLR 2018)**<br>
*Guillaume Lample, Alexis Conneau, Marc'Aurelio Ranzato, Ludovic Denoyer, Hervé Jégou*<br>
[[Paper]](https://openreview.net/pdf?id=H196sainb)
[[Code]](https://github.com/facebookresearch/MUSE)

### 4. RCSLS

**Loss in Translation: Learning Bilingual Word Mapping with a Retrieval Criterion (EMNLP 2018)**<br>
*Armand Joulin, Piotr Bojanowski, Tomas Mikolov, Hervé Jégou, Edouard Grave*<br>
[[Paper]](https://aclanthology.org/D18-1330/)
[[Code]](https://github.com/facebookresearch/fastText/tree/main/alignment)

### 5. VecMap

**A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings (ACL 2018)**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre*<br>
[[Paper]](https://aclanthology.org/P18-1073/)
[[Code]](https://github.com/artetxem/vecmap)

**Generalizing and Improving Bilingual Word Embedding Mappings with a Multi-Step Framework of Linear Transformations (AAAI 2018)**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre*<br>
[[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/11992)
[[Code]](https://github.com/artetxem/vecmap)

**Comments:** VecMap supports unsupervised (its ACL 2018 paper), semi-supervised and supervised (its AAAI 2018 paper) BLI settings.

# Recent Progress in BLI: Methodologies

### 1. ContrastiveBLI

**Improving Word Translation via Two-Stage Contrastive Learning (ACL 2022)**<br>
*Yaoyiran Li, Fangyu Liu, Nigel Collier, Anna Korhonen, Ivan Vulić*<br>
[[Paper]](https://arxiv.org/abs/2203.08307)
[[Code]](https://github.com/cambridgeltl/ContrastiveBLI)

**Comments:** New (2022) state-of-the-art method for semi-supervised and supervised BLI!

### 2. Prompt4BLI 

**On Bilingual Lexicon Induction with Large Language Models (EMNLP 2023)**<br>
*Yaoyiran Li, Anna Korhonen, Ivan Vulić*<br>
[[Paper]](https://arxiv.org/abs/2310.13995)
[[Code]](https://github.com/cambridgeltl/prompt4bli)

**Comments:** Prompt multilingual LLMs for BLI. Achieves new (2023) state-of-the-art BLI performance on many language pairs! A simple demo is provided in our sample code [./SampleCode.py](https://github.com/yaoyiran/Awesome-Bilingual-Lexicon-Induction-Papers-2022/blob/main/SampleCode.py).

### 3. BLISS

**Bilingual Lexicon Induction with Semi-supervision in Non-Isometric Embedding Spaces (ACL 2019)**<br>
*Barun Patra, Joel Ruben Antony Moniz, Sarthak Garg, Matthew R. Gormley, Graham Neubig*<br>
[[Paper]](https://aclanthology.org/P19-1018/)
[[Code]](https://github.com/joelmoniz/BLISS)

### 4. GeoMM

**Learning Multilingual Word Embeddings in Latent Metric Space: A Geometric Approach (TACL 2019)**<br>
*Pratik Jawanpuria, Arjun Balgovind, Anoop Kunchukuttan, Bamdev Mishra*<br>
[[Paper]](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00257/43509/Learning-Multilingual-Word-Embeddings-in-Latent)
[[Code]](https://github.com/anoopkunchukuttan/geomm)

### 5. LNMap

**LNMap: Departures from Isomorphic Assumption in Bilingual Lexicon Induction Through Non-Linear Mapping in Latent Space (EMNLP 2020)**<br>
*Tasnim Mohiuddin, M Saiful Bari, Shafiq Joty*<br>
[[Paper]](https://aclanthology.org/2020.emnlp-main.215/)
[[Code]](https://github.com/taasnim/lnmap)

### 6. InstaMap

**Non-Linear Instance-Based Cross-Lingual Mapping for Non-Isomorphic Embedding Spaces (ACL 2020)**<br>
*Goran Glavaš, Ivan Vulić*<br>
[[Paper]](https://aclanthology.org/2020.acl-main.675/)
[[Code]](https://github.com/codogogo/instamap)

### 7. CSCBLI

**Combining Static Word Embeddings and Contextual Representations for Bilingual Lexicon Induction (Findings of ACL 2021)**<br>
*Jinpeng Zhang, Baijun Ji, Nini Xiao, Xiangyu Duan, Min Zhang, Yangbin Shi, Weihua Luo*<br>
[[Paper]](https://aclanthology.org/2021.findings-acl.260/)
[[Code]](https://github.com/zjpbinary/CSCBLI)

### 8. mBERT

**It’s not Greek to mBERT: Inducing Word-Level Translations from Multilingual BERT (BlackboxNLP Workshop 2020)**<br>
*Hila Gonen, Shauli Ravfogel, Yanai Elazar, Yoav Goldberg*<br>
[[Paper]](https://aclanthology.org/2020.blackboxnlp-1.5/)
[[Code]](https://github.com/gonenhila/mbert)

### 9. IterNorm

**Are Girls Neko or Shōjo? Cross-Lingual Alignment of Non-Isomorphic Embeddings with Iterative Normalization (ACL 2019)**<br>
*Mozhi Zhang, Keyulu Xu, Ken-ichi Kawarabayashi, Stefanie Jegelka, Jordan Boyd-Graber*<br>
[[Paper]](https://aclanthology.org/P19-1307.pdf)
[[Code]](https://github.com/zhangmozhi/iternorm)

### 10. SpecNorm

**Normalization of Language Embeddings for Cross-Lingual Alignment (ICLR 2022)**<br>
*Prince Osei Aboaggye, Yan Zheng, Junpeng Wang, Michael Yeh, Wei Zhang, Liang Wang, Hao Yang, Jeff M. Phillips*<br>
[[Paper]](https://openreview.net/pdf?id=Nh7CtbyoqV5)
[[Code]](https://github.com/poaboagye/SpecNorm)

### 11. JointAlign

**Cross-lingual Alignment vs Joint Training: A Comparative Study and A Simple Unified Framework (ICLR 2020)**<br>
*Zirui Wang<sup>+</sup>, Jiateng Xie<sup>+</sup>, Ruochen Xu, Yiming Yang, Graham Neubig, Jaime Carbonell (+: equal contribution)*<br>
[[Paper]](https://arxiv.org/abs/1910.04708)
[[Code]](https://github.com/thespectrewithin/joint_align)

### 12. FIPP

**Filtered Inner Product Projection for Crosslingual Embedding Alignment (ICLR 2021)**<br>
*Vin Sachidananda, Ziyi Yang, Chenguang Zhu*<br>
[[Paper]](https://openreview.net/pdf?id=A2gNouoXE7)
[[Code]](https://github.com/vinsachi/FIPPCLE)

### 13. ClassyMap

**Classification-Based Self-Learning for Weakly Supervised Bilingual Lexicon Induction (ACL 2020)**<br>
*Mladen Karan, Ivan Vulić, Anna Korhonen, Goran Glavaš*<br>
[[Paper]](https://aclanthology.org/2020.acl-main.618/)
[[Code]](https://github.com/mladenk42/ClassyMap)

### 14. MUVE

**Visual Grounding in Video for Unsupervised Word Translation (CVPR 2020)**<br>
*Gunnar A. Sigurdsson, Jean-Baptiste Alayrac, Aida Nematzadeh, Lucas Smaira, Mateusz Malinowski, Joao Carreira, Phil Blunsom, Andrew Zisserman*<br>
[[Paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Sigurdsson_Visual_Grounding_in_Video_for_Unsupervised_Word_Translation_CVPR_2020_paper.html)
[[Code]](https://github.com/gsig/visual-grounding)

### 15. Bidirectional-RMP

**A Relaxed Matching Procedure for Unsupervised BLI (ACL 2020)**<br>
*Xu Zhao, Zihao Wang, Yong Zhang, Hao Wu*<br>
[[Paper]](https://aclanthology.org/2020.acl-main.274/)
[[Code]](https://github.com/BestActionNow/bidirectional-RMP)

### 16. (Methodology)

**A Graph-based Coarse-to-fine Method for Unsupervised Bilingual Lexicon Induction (ACL 2020)**<br>
*Shuo Ren, Shujie Liu, Ming Zhou, Shuai Ma*<br>
[[Paper]](https://aclanthology.org/2020.acl-main.318/)

### 17. CrossLingualELMo

**Cross-Lingual Alignment of Contextual Word Embeddings, with Applications to Zero-shot Dependency Parsing (NAACL 2019)**<br>
*Tal Schuster, Ori Ram, Regina Barzilay, Amir Globerson*<br>
[[Paper]](https://aclanthology.org/N19-1162/)
[[Code]](https://github.com/TalSchuster/CrossLingualContextualEmb)

### 18. (Methodology)

**Multilingual Alignment of Contextual Word Representations (ICLR 2020)**<br>
*Steven Cao, Nikita Kitaev, Dan Klein*<br>
[[Paper]](https://openreview.net/forum?id=r1xCMyBtPS)

### 19. Bitext-Lexind

**Bilingual Lexicon Induction via Unsupervised Bitext Construction and Word Alignment (ACL 2021)**<br>
*Haoyue Shi, Luke Zettlemoyer, Sida I. Wang*<br>
[[Paper]](https://aclanthology.org/2021.acl-long.67/)
[[Code]](https://github.com/facebookresearch/bitext-lexind)

### 20. Monoses

**Bilingual Lexicon Induction through Unsupervised Machine Translation (ACL 2019)**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre*<br>
[[Paper]](https://aclanthology.org/P19-1494/)
[[Code]](https://github.com/artetxem/monoses)

### 21. (Methodology)

**Unsupervised Alignment of Embeddings with Wasserstein Procrustes (AISTATS 2019)**<br>
*Edouard Grave, Armand Joulin, Quentin Berthet*<br>
[[Paper]](http://proceedings.mlr.press/v89/grave19a.html)
[[Code]](https://github.com/facebookresearch/fastText/tree/main/alignment)

### 22. OTAlign

**Gromov-Wasserstein Alignment of Word Embedding Spaces (EMNLP 2018)**<br>
*David Alvarez-Melis, Tommi Jaakkola*<br>
[[Paper]](https://aclanthology.org/D18-1214/)
[[Code]](https://github.com/dmelis/otalign)

### 23. L1-Refinement

**Cross-Lingual Word Embedding Refinement by ℓ1 Norm Optimisation (NAACL 2021)**<br>
*Xutan Peng, Chenghua Lin, Mark Stevenson*<br>
[[Paper]](https://aclanthology.org/2021.naacl-main.214/)
[[Code]](https://github.com/Pzoom522/L1-Refinement)

### 24. (Methodology)

**A Simple and Effective Approach to Robust Unsupervised Bilingual Dictionary Induction (COLING 2020)**<br>
*Yanyang Li, Yingfeng Luo, Ye Lin, Quan Du, Huizhen Wang, Shujian Huang, Tong Xiao, Jingbo Zhu*<br>
[[Paper]](https://aclanthology.org/2020.coling-main.526/)


### 25. ContextualMapping

**Cross-Lingual BERT Contextual Embedding Space Mapping with Isotropic and Isometric Conditions (arXiv 2021)**<br>
*Haoran Xu, Philipp Koehn*<br>
[[Paper]](https://arxiv.org/pdf/2107.09186.pdf)
[[Code]](https://github.com/fe1ixxu/Contextual_Mapping)

### 26. BDMA

**Learning a Reversible Embedding Mapping using Bi-Directional Manifold Alignment (Findings of ACL 2021)**<br>
*Ashwinkumar Ganesan, Francis Ferraro, Tim Oates*<br>
[[Paper]](https://aclanthology.org/2021.findings-acl.276/)
[[Code]](https://github.com/codehacken/bdma)

### 27. CLIME

**Interactive Refinement of Cross-Lingual Word Embeddings (EMNLP 2020)**<br>
*Michelle Yuan<sup>+</sup>, Mozhi Zhang<sup>+</sup>, Benjamin Van Durme, Leah Findlater, Jordan Boyd-Graber (+: equal contribution)*<br>
[[Paper]](https://aclanthology.org/2020.emnlp-main.482.pdf)
[[Code]](https://github.com/forest-snow/clime-ui)

### 28. BLICEr

**Improving Bilingual Lexicon Induction with Cross-Encoder Reranking (Findings of EMNLP 2022)**<br>
*Yaoyiran Li, Fangyu Liu, Ivan Vulić<sup>+</sup>, Anna Korhonen<sup>+</sup> (+: equal contribution)*<br>
[[Paper]](https://arxiv.org/abs/2210.16953)
[[Code]](https://github.com/cambridgeltl/BLICEr)

### 29. IsoVec

**IsoVec: Controlling the Relative Isomorphism of Word Embedding Spaces (EMNLP 2022)**<br>
*Kelly Marchisio, Neha Verma, Kevin Duh, Philipp Koehn*<br>
[[Paper]](https://aclanthology.org/2022.emnlp-main.404/)
[[Code]](https://github.com/kellymarchisio/isovec)

### 30. Dual-BLI

**Dual Word Embedding for Robust Unsupervised Bilingual Lexicon Induction (TASLP 2023)**<br>
*Hailong Cao, Liguo Li, Conghui Zhu, Muyun Yang, Tiejun Zhao*<br>
[[Paper]](https://ieeexplore.ieee.org/abstract/document/10167848/authors)
[[Code]](https://github.com/liguo-cs/Dual-BLI.git)


### 31. CD-BLI

**CD-BLI: Confidence-Based Dual Refinement for Unsupervised Bilingual Lexicon Induction (NLPCC 2023)**<br>
*Shenglong Yu, Wenya Guo, Ying Zhang, Xiaojie Yuan*<br>
[[Paper]](https://link.springer.com/chapter/10.1007/978-3-031-44696-2_30)

### 32. RAPO

**RAPO: An Adaptive Ranking Paradigm for Bilingual Lexicon Induction (EMNLP 2022)**<br>
*Zhoujin Tian, Chaozhuo Li, Shuo Ren, Zhiqiang Zuo, Zengxuan Wen, Xinyue Hu, Xiao Han, Haizhen Huang, Denvy Deng, Qi Zhang, Xing Xie*<br>
[[Paper]](https://aclanthology.org/2022.emnlp-main.606/)
[[Code]](https://github.com/Jlfj345wf/RAPO)

### 33. ProMap

**ProMap: Effective Bilingual Lexicon Induction via Language Model Prompting (IJCNLP-AACL 2023)**<br>
*Abdellah El Mekki, Muhammad Abdul-Mageed, ElMoatez Billah Nagoudi, Ismail Berrada, Ahmed Khoumsi*<br>
[[Paper]](https://arxiv.org/abs/2310.18778)
[[Code]](https://github.com/4mekki4/promap)

### 34. SAGAN

**A Structure-Aware Generative Adversarial Network for Bilingual Lexicon
Induction (Findings of EMNLP 2023)**<br>
*Bocheng Han, Qian Tao, Lusi Li, Zhihao Xiong*<br>
[[Paper]](https://aclanthology.org/2023.findings-emnlp.721/)
[[Code]](https://github.com/scutBCH/SAGAN)

### 35. Goat-for-BLI

**Bilingual Lexicon Induction for Low-Resource Languages using Graph Matching via Optimal Transport (EMNLP 2022)**<br>
*Kelly Marchisio, Ali Saad-Eldin, Kevin Duh, Carey Priebe, Philipp Koehn*<br>
[[Paper]](https://aclanthology.org/2022.emnlp-main.164/)
[[Code]](https://github.com/kellymarchisio/goat-for-bli)

### 36. HCEG

**Hierarchical Mapping for Crosslingual Word Embedding Alignment (TACL 2020)**<br>
*Ion Madrazo Azpiazu, Maria Soledad Pera*<br>
[[Paper]](https://aclanthology.org/2020.tacl-1.24/)
[[Code]](https://github.com/ionmadrazo/HCEG)

### 37. SAIL

**Self-Augmented In-Context Learning for Unsupervised Word Translation (ACL 2024)**<br>
*Yaoyiran Li, Anna Korhonen, Ivan Vulić*<br>
[[Paper]](https://arxiv.org/abs/2402.10024)
[[Code]](https://github.com/cambridgeltl/sail-bli)

### 38. LFBB

**How Lexical is Bilingual Lexicon Induction? (Findings of NAACL 2024)**<br>
*Harsh Kohli, Helian Feng, Nicholas Dronen, Calvin McCarter, Sina Moeini, Ali Kebarighotbi*<br>
[[Paper]](https://arxiv.org/abs/2404.04221)

### 39. BRTR/BRSR  

**Enhancing Bilingual Lexicon Induction via Bi-directional Translation Pair Retrieving (AAAI 2024)**<br>
*Qiuyu Ding, Hailong Cao, Tiejun Zhao*<br>
[[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/29744)

### 40. (Methodology)

**When Your Cousin Has the Right Connections: Unsupervised Bilingual Lexicon Induction for Related Data-Imbalanced Languages (LREC-COLING 2024)**<br>
*Niyati Bafna, Cristina España-Bonet, Josef van Genabith, Benoît Sagot, Rachel Bawden*<br>
[[Paper]](https://aclanthology.org/2024.lrec-main.1526/)

### 41. LexGen

**LexGen: Domain-aware Multilingual Lexicon Generation (arXiv 2024)**<br>
*Karthika NJ, Ayush Maheshwari, Atul Kumar Singh, Preethi Jyothi, Ganesh Ramakrishnan, Krishnakant Bhatt*<br>
[[Paper]](https://arxiv.org/abs/2405.11200)

### 42. DM-BLI

**DM-BLI: Dynamic Multiple Subspaces Alignment for Unsupervised Bilingual Lexicon Induction (ACL 2024)**<br>
*Ling Hu, Yuemei Xu*<br>
[[Paper]](https://aclanthology.org/2024.acl-long.112/)
[[Code]](https://github.com/huling-2/DM-BLI)


# Recent Progress in BLI: Datasets, Benchmarks, Analyses & Surveys
### 1. XLING (Dataset)

**How to (Properly) Evaluate Cross-Lingual Word Embeddings: On Strong Baselines, Comparative Analyses, and Some Misconceptions (ACL 2019)**<br>
*Goran Glavaš, Robert Litschko, Sebastian Ruder, Ivan Vulić*<br>
[[Paper]](https://aclanthology.org/P19-1070/)
[[Code]](https://github.com/codogogo/xling-eval)

### 2. Panlex-BLI (Dataset)

**Do We Really Need Fully Unsupervised Cross-Lingual Embeddings? (EMNLP 2019)**<br>
*Ivan Vulić, Goran Glavaš, Roi Reichart, Anna Korhonen*<br>
[[Paper]](https://aclanthology.org/D19-1449/)
[[Code]](https://github.com/cambridgeltl/panlex-bli)

### 3. (Analysis)
**On the Limitations of Unsupervised Bilingual Dictionary Induction (ACL 2018)**<br>
*Anders Søgaard, Sebastian Ruder, Ivan Vulić*<br>
[[Paper]](https://aclanthology.org/P18-1072/)

### 4. ISO-Study

**Are All Good Word Vector Spaces Isomorphic? (EMNLP 2020)**<br>
*Ivan Vulić, Sebastian Ruder, Anders Søgaard*<br>
[[Paper]](https://aclanthology.org/2020.emnlp-main.257/)
[[Code]](https://github.com/cambridgeltl/iso-study)

### 5. (Survey)

**A Survey of Cross-Lingual Word Embedding Models (JAIR 2019)**<br>
*Sebastian Ruder, Ivan Vulić, Anders Søgaard*<br>
[[Paper]](https://www.jair.org/index.php/jair/article/view/11640)

### 6. Embeddings (Dataset)

**Should All Cross-Lingual Embeddings Speak English? (ACL 2020)**<br>
*Antonios Anastasopoulos, Graham Neubig*<br>
[[Paper]](https://aclanthology.org/2020.acl-main.766/)
[[Code]](https://github.com/antonisa/embeddings)

### 7. xANLG (Analysis)

**Understanding Linearity of Cross-Lingual Word Embedding Mappings (TMLR 2022)**<br>
*Xutan Peng, Mark Stevenson, Chenghua Lin, Chen Li*<br>
[[Paper]](https://openreview.net/pdf?id=8HuyXvbvqX)
[[Code]](https://github.com/Pzoom522/xANLG)

# Applications of BLI in Machine Translation, Cross-lingual Transfer Learning, etc.

### 1. (Application)

**Dictionary-based phrase-level prompting of large language models for machine translation (arXiv 2023)**<br>
*Marjan Ghazvininejad, Hila Gonen, Luke Zettlemoyer*<br>
[[Paper]](https://arxiv.org/abs/2302.07856)

### 2. (Application)

**Improving Zero-Shot Cross-lingual Transfer for Multilingual Question Answering over Knowledge Graph (NAACL 2021)**<br>
*Yucheng Zhou, Xiubo Geng, Tao Shen, Wenqiang Zhang, Daxin Jiang*<br>
[[Paper]](https://aclanthology.org/2021.naacl-main.465/)

### 3. (Application)

**Cross-Cultural Similarity Features for Cross-Lingual Transfer Learning of Pragmatically Motivated Tasks (EACL 2021)**<br>
*Jimin Sun, Hwijeen Ahn, Chan Young Park, Yulia Tsvetkov, David R. Mortensen*<br>
[[Paper]](https://aclanthology.org/2021.eacl-main.204/)

### 4. (Application)

**Unsupervised Neural Machine Translation (ICLR 2018)**<br>
*Mikel Artetxe, Gorka Labaka, Eneko Agirre, Kyunghyun Cho*<br>
[[Paper]](https://openreview.net/forum?id=Sy2ogebAW)

### 5. (Application)

**When Does Unsupervised Machine Translation Work? (WMT 2020)**<br>
*Kelly Marchisio, Kevin Duh, Philipp Koehn*<br>
[[Paper]](https://aclanthology.org/2020.wmt-1.68/)

### 6. (Application)

**Improving the Lexical Ability of Pretrained Language Models for Unsupervised Neural Machine Translation (NAACL 2021)**<br>
*Alexandra Chronopoulou, Dario Stojanovski, Alexander Fraser*<br>
[[Paper]](https://aclanthology.org/2021.naacl-main.16/)

### 7. (Application)

**CJE-TIG: Zero-shot cross-lingual text-to-image generation by Corpora-based Joint Encoding (Knowledge-Based Systems 2022)**<br>
*Han Zhang, Suyi Yang, Hongqing Zhu*<br>
[[Paper]](https://www.sciencedirect.com/science/article/pii/S0950705121011138?via=ihub)

# Pull Requests Are Welcome:

### No.

**()**<br>
**<br>
[[Paper]]()
[[Code]]()

**Comments:**

