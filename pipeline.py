# Pipeline orchestrates and collects data and performance metrics from the retrievers. This is the point of access for the project.
import path_setup

path_setup.ensure_project_root_on_path()

import yaml  # load retriever configs
from rank_bm25 import BM25Okapi # use rank_bm25 for BM25 variants from venv/lib/python3.8/site-packages/rank_bm25.py 

from config.BEIR import BEIR #corpus, queries and qrels in shape corpus = [d₁, d₂, d₃, ..., dₙ]

def tokenizer(text):
    return text.split()  # split on each doc where corpus is containing d=1 to n, each split by tokenizer
    # corpus = 
    # [
    # ["This", is", "doc1"...],
    # ["Another", "document"...],
    # ["More", "text", "here"...]
    # ]


beir = BEIR(dataset_name="scidocs", from_=0, to_=1)
print(type(beir.corpus))

## Corpus 
documents = [ doc["title"]+" "+ doc["text"] for doc in beir.corpus]
tokenized_corpus = [tokenizer(doc) for doc in documents]
## Query 
query_text = beir.queries[0]["text"]
tokenized_query = tokenizer(query_text)
# Retrieval 
bm25Okapi= BM25Okapi(tokenized_corpus)


out = bm25Okapi.get_top_n(tokenized_query, documents, n=3) #retruns a list of top n docs
top_n_corpus_id=[]
for o in out:
    oo=beir.corpus_dict.get(o)
    top_n_corpus_id.append(oo)

print(out)
print(top_n_corpus_id)


# config loading 
'''
bm25_config = yaml.safe_load(open('config/bm25_config.yaml'))

def bm25_init(config_input):
    retrievers_out=[]
    for retriever in config_input['retriever']:
        r = getattr(rank_bm25, retriever) 
        retrievers_out.append(r)
    return retrievers_out


def bm25_runner(function_name):  # calls respective interface in the bm25 lib
    pass

retrievers=[] # list of retriver classes built on config

'''


    

