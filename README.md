This project is WIP

###Data transformation notes 

#### BM25
    ##### 1. Tokenizer: Splits into words for each document d:

    ##### split on each doc where corpus is containing d=1 to n, each split by tokenizer
        # corpus = 
        # [
        # ["this", is", "doc1"],
        # ["another", "document"],
        # ["more", "text", "here"]
        # ]
    ##### 2. HF retuning datast -> tokenized -> iterate each d in BM25_tokenize_corpus

### Reference 

Corpus reference [BeIR/scidocs] : https://huggingface.co/datasets/BeIR/scidocs/viewer/corpus/corpus ; https://huggingface.co/datasets/BeIR/scidocs/blob/main/README.md 

R reference: BeIR/scidocs-qrels: https://huggingface.co/datasets/BeIR/scidocs-qrels 