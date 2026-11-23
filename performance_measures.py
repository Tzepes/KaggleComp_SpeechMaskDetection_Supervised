# A list of performance measures that would be fitting for this problem.
# The task itself is a binary classification supervised task.

#MAE

#MSE

#Binary Closs Entropy Loss

#The rest will be chosen based on used models

#Schuller et al 2009 suggests Unweighted Average Recall (UAR), it is more adequate for (unbalanced) multi-class classifications than Weighted Average Recal
#   scikit-learn does not have a dedicated unweighted_average_recall function in its core metrics module, it can be computed using the recall_score function with the average='macro' parameter
#   The recall score is tp / (tp + fn) 
#   The recall is intuitively the ability of the classifier to find all the positive samples.

