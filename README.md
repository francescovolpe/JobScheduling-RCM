# JobScheduling-RCM

### Obiettivi
1. Data una pianificazione dei tempi di lavoro e le capacità degli operai ci si chiede se è possibile svolgere le attività di costruzione nei tempi stabiliti e stabilire la pianificazione del lavoro degli operai ([CSP.ipynb](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/CSP.ipynb))

2. Stimare i costi relativi alla costruzione di una casa dati i tempi di completamento delle attività ([AI.ipynb](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/AI.ipynb))


### Algoritmi utilizzati
1. Ragionamento con vincoli + algoritmi di ricerca su grafo
2. Algoritmi di regressione lineare, alberi di regressione, random forest


### Ragionamento con vincoli
- AIPython
- Dati: attività, # case, specializzazione degli operai
- Trasformazione del problema in un CSP da risolvere
- Costruzione di variabili con domini e definizione dei vincoli

### Variabili e vincoli
Variabili:	«giorno_#casa_attività»
- G1_casa1_sistemazioneDellaStrada
  - dom(Andrea,Paolo, …)
- G1_casa2_muratura				
  - dom(Andrea,Nicola, …)

Vincoli: un operaio non può nello stesso giorno svolgere più attività contemporaneamente

### Attività
- Ordine attività modellate come un grafo
- Per ogni nodo (attività) vi è associato un numero di giorni per il completamento
- Obiettivo ricavare le variabili
- Esplorazione del grafo con una ricerca in ampiezza per individuare il tempo di inizio di un’attività (percorso massimo fino a quel nodo)

![GrafoAttività](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/Img/Grafo.png)

### Output
- Risoluzione tramite algoritmo di ricerca (AIPyhton)
- Output:
  - 'G3_C0_010': '0002',
  - 'G4_C0_010': '0001',
  - 'G5_C0_010': '0002’,

### Apprendimento
- scikit-learn
- Dataset: 1000 record (creato per testare l'algoritmo)
- Colonne indicano le attività [1-14]
- Colonna costo indica il costo effettivo
- Valori indicano i tempi richiesti per quell’attività

#### Risultati Regressione lineare
![RegressioneLineare](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/Img/RegressioneLineare.png)

#### Risultati Alberi di regressione e random forest
![Alberi&RandomForest](https://github.com/francescovolpe/JobScheduling-RCM/blob/main/Img/Alberi%26RandomForest.png)

### Problemi visualizzazione notebook
Se riscontri problemi nella visualizzazione dei notebook a causa del rendering, puoi utilizzare [nbviewer](https://nbviewer.jupyter.org/)
