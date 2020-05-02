import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# define samples this way as scipy.stats.wasserstein_distance can't take probability distributions directly
sampP = [2,2,2,2,2,2,4,6,8,10]
sampQ = [2,4,5,8,10,10,10,10,10,10,]
# and for scipy.stats.entropy (gives KL divergence here) we want distributions
P = np.unique(sampP, return_counts=True)[1] / len(sampP)
Q = np.unique(sampQ, return_counts=True)[1] / len(sampQ)
# compare to this sample / distribution:
sampQ2 = [2,4,4,4,4,4,4,6,8,10]
Q2 = np.unique(sampQ2, return_counts=True)[1] / len(sampQ2)

# fig = plt.figure(figsize=(10,7))
# fig.subplots_adjust(wspace=0.5)
fig = plt.figure()
plt.subplot(2,1,1)
plt.title("Earth Mover Distance = {:.4}\nKL divergence= {:.4}".format(
    scipy.stats.wasserstein_distance(sampP, sampQ), scipy.stats.entropy(P, Q)), fontsize=12)
plt.bar(np.arange(len(P)), P, color='#176BA0')
plt.xticks(np.arange(len(P)), np.arange(1,5), fontsize=0)
plt.subplot(2,1,2)
plt.bar(np.arange(len(Q)), Q, color='#AF4BCE')
plt.xticks(np.arange(len(Q)), np.arange(1,5))

fig2 = plt.figure()
plt.subplot(2,1,1)
plt.title("Earth Mover Distance = {:.4}\nKL divergence= {:.4}".format(
    scipy.stats.wasserstein_distance(sampP, sampQ2), scipy.stats.entropy(P, Q2)), fontsize=12)
plt.bar(np.arange(len(P)), P, color='#176BA0')
plt.xticks(np.arange(len(P)), np.arange(1,5), fontsize=0)
plt.subplot(2,1,2)
plt.bar(np.arange(len(Q2)), Q2, color='#AF4BCE')
plt.xticks(np.arange(len(Q2)), np.arange(1,5))

plt.show()