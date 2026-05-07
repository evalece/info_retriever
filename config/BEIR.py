
from datasets import load_dataset
import logging 

# debug 
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO) # logger filtering control; aside: DEBUG < INFO < WARNING < ERROR < CRITICAL, 

logging.basicConfig(
    level=logging.INFO, # aside: DEBUG < INFO < WARNING < ERROR < CRITICAL, 
    format="%(levelname)s%(name)s:\n%(message)s\n"
    )


class BEIR:
    def __init__(self, dataset_name, from_=0, to_=1,split= "test"): # from and to are in %  in loading train/test/validation sets 
        self.split= split
        self.from_= from_
        self.to_ = to_  
        self.dataset_name = 'BeIR/'+ dataset_name #i.e., dataset_name= scidocs
        self.corpus_dict={}
        self.queries_dict={}
        self.corpus = self.load_corpus() # d; need to load full documents for information retrieval 
        self.queries = self.load_queries() # q; can load partial  
        self.qrels = self.load_qrels() # loading of T for identifying relevance 
        

    
    def load_corpus(self):
        d = load_dataset(self.dataset_name, "corpus") # HF returns datadict, need parse by passing 'corpus' key

        for i in d["corpus"]:
            self.corpus_dict[(i["title"] or " ")+" "+i["text"]] = i["_id"]
        
        logger.info("load_corpus: %s", d["corpus"][:3])
        key = next(iter(self.corpus_dict))
        logger.info("sample of id in corps:\n%s", {key: self.corpus_dict[key]})
        return d["corpus"]

    def load_queries(self): # construct a dict for quries using dataset _id
        d = load_dataset(self.dataset_name,'queries')
        for i in d["queries"]:
            self.queries_dict[i["text"]] = i["_id"]
        logger.info("load_queries: %s", d['queries']['text'][:3])
        return d["queries"]["text"]

    def load_qrels(self):
        d=load_dataset(self.dataset_name+"-qrels", split= self.split)  # need to get all due to schema restrictions ->, split= f"{self.split}[{self.from_}%:{self.to_}%](pct1_dropremainder)") # train, validation, test; ref: https://huggingface.co/docs/datasets/loading 
        logging.info("load_qrels: %s", d[:3])
        return d

    
b= BEIR(dataset_name='scidocs') # example usage 