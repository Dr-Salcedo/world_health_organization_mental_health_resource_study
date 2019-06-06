import numpy as np
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

def bootstrap_and_compare(samp1, samp2, num_bootstraps=1000, size_bootstraps=500):
    
    samp1_bootstraps = []
    for i in range(num_bootstraps):
        samp1_bootstraps.append(np.random.choice(samp1, size_bootstraps, replace=True))

    samp1_means = []
    for i in samp1_bootstraps:
        samp1_means.append(np.mean(i))
    
    samp2_bootstraps = []
    for i in range(num_bootstraps):
        samp2_bootstraps.append(np.random.choice(samp2, size_bootstraps, replace=True))

    samp2_means = []
    for i in samp2_bootstraps:
        samp2_means.append(np.mean(i))
    
    sns.distplot(samp1_means, color='red', label="above mean")
    sns.distplot(samp2_means, label="below mean")
    plt.legend()
    
    test = ttest_ind(samp1_means, samp2_means, equal_var=False)
    
    if test[1] < .05:
        print("With p={}, we can reject the Null Hypothesis. These populations are different.".format(test[1]))
        
    if test[1] >= .05:
        print("With p={}, we cannot reject the Null Hypothesis. We didn't find evidence that these populations are different.".format(test[1]))
    
    return ttest_ind(samp1_means, samp2_means, equal_var=False)