#!/usr/bin/env python
# coding: utf-8

# In[1]:


#add this line for interactive plotting
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


#dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[ ]:


#set x-axis to compare (1)Capomulin, (2)Infubinol, (3)Ketapril, and (4)Placebo
x_axis = np.arange(1, 5, 1)
x_axis


# In[3]:


# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')


# In[4]:


# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"


# In[5]:


# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_drug_data_to_load_df = pd.read_csv(mouse_drug_data_to_load, encoding="utf-8")
clinical_trial_data_to_load = pd.read_csv(clinical_trial_data_to_load, encoding="utf-8")


# In[16]:


# Combine the data into a single dataset
df_mouse = pd.DataFrame({"Mouse ID": Mouse,
                               "Drug": Drug}
                                         )
df_clinical = pd.DataFrame({"Mouse ID": Mouse,
                                  "Timepoint": Timepoint,
                                  "Tumor Volume (mm3)": Size,
                                  "Metastatic Sites": Metastatic}
                                             )
                                             
merged_df = pd.merge(mouse_drug_data_to_load_df, clinical_trial_data_to_load_df)


# In[17]:


# Display the data table for preview
merged_df.head()


# In[ ]:




