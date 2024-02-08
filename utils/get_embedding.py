import pandas as pd
import torch

def string_to_embedding_old(trial_info): 
   
   # loading all the key information
   embedding_type = trial_info["embedding_type"]
   feature_n = trial_info["feature_n"]
   fam = trial_info['fam'] 
   test = trial_info['test']

   print(fam)
   print(test)


   # loading the corresponding embedding file
   if embedding_type == "resnet_pa": 
      embeddings = pd.read_csv("RANCH_cluster/sim_info/embeddings/resnet_pa.csv", header=None)
   
   elif embedding_type == "resnet50":
         embeddings = pd.read_csv("RANCH_cluster/sim_info/embeddings/resnet50.csv", header=None)

   elif embedding_type == "resnet_saycam":
      embeddings = pd.read_csv("RANCH_cluster/sim_info/embeddings/resnet_pa.csv")

   fam_raw = embeddings[embeddings.iloc[:,0] == fam]
   test_raw =  embeddings[embeddings.iloc[:,0] == test]

   f_val = torch.tensor(fam_raw.iloc[:, 1:feature_n+1].values[0])
   t_val = torch.tensor(test_raw.iloc[:, 1:feature_n+1].values[0])

   return (f_val, t_val)

def string_to_embedding(trial_info, embedding_csv): 
   
   # loading all the key information
   feature_n = trial_info["feature_n"]
   fam = trial_info['fam'] 
   test = trial_info['test']

   print(fam)
   print(test)
   embeddings = pd.read_csv(embedding_csv, header=None)

   fam_raw = embeddings[embeddings.iloc[:,0] == fam]
   test_raw =  embeddings[embeddings.iloc[:,0] == test]

   f_val = torch.tensor(fam_raw.iloc[:, 1:feature_n+1].values[0])
   t_val = torch.tensor(test_raw.iloc[:, 1:feature_n+1].values[0])

   return (f_val, t_val)




   
#elif: 
   


