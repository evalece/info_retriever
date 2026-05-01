from datasets import load_dataset



class BEIR:
    def __init__(self, dataset_name, split= "train"):
        self.split= split
        self.dataset_name = "BeIR/"+ dataset_name #i.e., dataset_name= scidocs
        self.corpus = self.load_corpus() # d; need to load full documents for information retrieval 
        self.queries = self.load_queries() # q; can load partial 
        self.queries_percentage= 0.01 
        self.qrels = self.load_qrels() # loading of T for identifying relevance 

    def load_corpus(self):
        return load_dataset(self.dataset_name, "corpus")

    def load_queries(self):
        return load_dataset(self.dataset_name, "queries")

    def load_qrels(self):
        return load_dataset(self.dataset_name+"-qrels", split=self.split) # train, validation, test 
    
  