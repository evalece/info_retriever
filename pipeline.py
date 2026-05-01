# Pipeline orchestrates and collects data and performance metrics from the retrievers. This is the point of access for the project.
import yaml # load retriever configs
import rank_bm25 # use rank_bm25 for BM25 variants

config = yaml.safe_load(open('config/config.yaml'))

def bm25_init(config_input):
    retrievers_out=[]
    for retriever in config_input['retriever']:
        r = getattr(rank_bm25, retriever) 
        retrievers_out.append(r)
    return retrievers_out


def bm25_runner(function_name): # calls respective iterface in the bm 25 lib 
    pass
    
    
retrievers=[] # list of retriver classes built on config


    

