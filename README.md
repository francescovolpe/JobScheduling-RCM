# JobScheduling-RCM

### Objectives
1. Given a work schedule and the capabilities of the workers, the question arises whether it is possible to carry out the construction activities on time and establish the work schedule of the workers ([CSP.ipynb](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/CSP.ipynb))

2. Estimate the costs related to the construction of a house given the time frame for completion ([AI.ipynb](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/AI.ipynb))


### Algorithms used
1. Reasoning with constraints + graph search algorithms
2. Linear regression algorithms, regression trees, random forests


### Reasoning with constraints
- AIPython
- Data: activities, # houses, workers' specialisation
- Transforming the problem into a CSP to be solved
- Construction of variables with domains and definition of constraints

### Variables and constraints
Variables:	«giorno_#casa_attività»
- G1_casa1_sistemazioneDellaStrada
  - dom(Andrea,Paolo, …)
- G1_casa2_muratura				
  - dom(Andrea,Nicola, …)

Constraints: a worker may not perform several activities at the same time on the same day

### Activities
- Ordering activities modelled as a graph
- For each node (activity) there is an associated number of days for completion
- Objective to derive variables
- Graph exploration with a breadth-first search for the start time of an activity (maximum path to that node)

![GrafoAttività](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/Img/Grafo.png)

### Output
- Resolution by search algorithm (AIPyhton)
- Output:
  - 'G3_C0_010': '0002',
  - 'G4_C0_010': '0001',
  - 'G5_C0_010': '0002’,

### Learning
- Scikit-learn & Pandas
- Dataset: 1000 record (created to test the algorithm)
- Columns indicate activities [1-14]
- Cost column indicates actual cost
- Values indicate the time required for that activity

#### Results Linear regression
![RegressioneLineare](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/Img/RegressioneLineare.png)

#### Results Regression trees and random forests
![Alberi&RandomForest](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/Img/Alberi%26RandomForest.png)

### Notebook display problems
If you experience problems displaying notebooks due to rendering, you can use [nbviewer](https://nbviewer.jupyter.org/)
