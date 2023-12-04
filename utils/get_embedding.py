import pandas as pd
import torch

def string_to_embedding(trial_info): 
   
   # loading all the key information
   embedding_type = trial_info["embedding_type"]
   feature_n = trial_info["feature_n"]
   background = trial_info['background'] 
   deviant = trial_info['deviant']


   # loading the corresponding embedding file
   if embedding_type == "resnet_pa": 
      embeddings = pd.read_csv("sim_info/embeddings/resnet_pa.csv")
   elif embedding_type == "resnet_saycam":
      embeddings = pd.read_csv("../sim_info/embeddings/resnet_pa.csv")

   background_raw = embeddings[embeddings.iloc[:,0] == background]
   deviant_raw =  embeddings[embeddings.iloc[:,0] == deviant]

   b_val = torch.tensor(background_raw.iloc[:, 1:feature_n+1].values[0])
   d_val = torch.tensor(deviant_raw.iloc[:, 1:feature_n+1].values[0])

   return (b_val, d_val)




   
#elif: 
   


