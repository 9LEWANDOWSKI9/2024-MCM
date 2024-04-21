from hmmlearn import hmm
import numpy as np
import pandas as pd
from hmmlearn import hmm

df = pd.read_csv('match_2023-wimbledon-1701.csv')

observations = df['point_victor'].values.reshape(-1, 1)
hmm_model = hmm.MultinomialHMM(n_components=2, n_iter=100)

hmm_model.fit(observations)

hidden_states = hmm_model.predict(observations)

print("初始状态概率分布：", hmm_model.startprob_)
print("状态转移概率矩阵：", hmm_model.transmat_)
print("观测概率矩阵：", hmm_model.emissionprob_)
print("预测的隐藏状态序列：", hidden_states)
