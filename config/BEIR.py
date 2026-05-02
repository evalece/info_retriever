
from datasets import load_dataset
import logging 

# debug 
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO) # logger filtering control; aside: DEBUG < INFO < WARNING < ERROR < CRITICAL, 

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s%(name)s:\n%(message)s\n"
    )


class BEIR:
    def __init__(self, dataset_name, from_=0, to_=1,split= "test"): # from and to are in %  in loading train/test/validation sets 
        self.split= split
        self.from_= from_
        self.to_ = to_  
        self.dataset_name = 'BeIR/'+ dataset_name #i.e., dataset_name= scidocs
        self.corpus = self.load_corpus() # d; need to load full documents for information retrieval 
        self.queries = self.load_queries() # q; can load partial  
        self.qrels = self.load_qrels() # loading of T for identifying relevance 
 

    
    
    def load_corpus(self):
        d = load_dataset(self.dataset_name, "corpus")
        logger.info("load_corpus: %s", d["corpus"][:1])
        return d

    def load_queries(self):
        d = load_dataset(self.dataset_name, "queries")
        logger.info("load_queries: %s", d["queries"][:1])
        return d["queries"]

    def load_qrels(self):
        d=load_dataset(self.dataset_name+"-qrels", split= f"{self.split}[{self.from_}%:{self.to_}%](pct1_dropremainder)") # train, validation, test; ref: https://huggingface.co/docs/datasets/loading 
        logging.info(d[:1])
        return d

    
b= BEIR(dataset_name='scidocs')