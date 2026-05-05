This project is WIP

### Data transformation notes 

#### BM25
##### 1. Tokenizer: Splits into words for each document d:
 split on each doc where corpus is containing d=1 to n, each split by tokenizer

        # corpus = 
        # [
        # ["this", is", "doc1"],
        # ["another", "document"],
        # ["more", "text", "here"]
        # ]


##### 2. HF retuning datast -> tokenized -> iterate each d in BM25_tokenize_corpus


##### 3. Progress:
- Calculating precision and recall in progress

Debug output

['A Hybrid EP and SQP for Dynamic Economic Dispatch with Nonsmooth Fuel Cost Function Dynamic economic dispatch (DED) is one of the main functions of power generation operation and control. It determines the optimal settings of generator units with predicted load demand over a certain period of time. The objective is to operate an electric power system most economically while the system is operating within its security limits. This paper proposes a new hybrid methodology for solving DED. The proposed method is developed in such a way that a simple evolutionary programming (EP) is applied as a based level search, which can give a good direction to the optimal global region, and a local search sequential quadratic programming (SQP) is used as a fine tuning to determine the optimal solution at the final. Ten units test system with nonsmooth fuel cost function is used to illustrate the effectiveness of the proposed method compared with those obtained from EP and SQP alone.', 'Distributed Event-Triggered Scheme for Economic Dispatch in Smart Grids To reduce information exchange requirements in smart grids, an event-triggered communication-based distributed optimization is proposed for economic dispatch. In this work, the θ-logarithmic barrier-based method is employed to reformulate the economic dispatch problem, and the consensus-based approach is considered for developing fully distributed technology-enabled algorithms. Specifically, a novel distributed algorithm utilizes the minimum connected dominating set (CDS), which efficiently allocates the task of balancing supply and demand for the entire power network at the beginning of economic dispatch. Further, an event-triggered communication-based method for the incremental cost of each generator is able to reach a consensus, coinciding with the global optimality of the objective function. In addition, a fast gradient-based distributed optimization method is also designed to accelerate the convergence rate of the event-triggered distributed optimization. Simulations based on the IEEE 57-bus test system demonstrate the effectiveness and good performance of proposed algorithms.', 'The Granular Tabu Search and Its Application to the Vehicle-Routing Problem ']
['86e87db2dab958f1bd5877dc7d5b8105d6e31e46', '2a43d3905699927ace64e880fe9ba8a730e14be1', '697754f7e62236f6a2a069134cbc62e3138ac89f']

### Reference  

Corpus reference [BeIR/scidocs] : https://huggingface.co/datasets/BeIR/scidocs/viewer/corpus/corpus ; https://huggingface.co/datasets/BeIR/scidocs/blob/main/README.md 

R reference: BeIR/scidocs-qrels: https://huggingface.co/datasets/BeIR/scidocs-qrels 