# Final Project
## Stephanie Ong
### 12/9/2025

#### Q1
import pandas as pd
import numpy as np
import altair as alt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

s = pd.read_csv("social_media_usage.csv")
print(s.shape)

#import streamlit as st

#st.markdown("# My streamlit data science app!!!")