# **1. Part 1** #

**SPAM Dataset**

For Spam Data:
Precision = 0.9469
Recall=0.9834
Fscore=0.9648

For HAM Data:
Precision = 0.9939
Recall=0.98
Fscore=0.9869

**SENTIMENT Dataset**

For Pos Data:
Precision = 0.8412
Recall=0.8831
Fscore=0.8616

For Neg Data:
Precision = 0.8734
Recall=0.812
Fscore=0.8416


# **2.  Part 2:** #

**Using SVM**

**SPAM Dataset**

For Spam Data:
Precision = 0.95681
Recall=0.7933
Fscore=0.8674

For HAM Data:
Precision = 0.9293
Recall=0.987
Fscore=0.9573

**SENTIMENT Dataset**

For Pos Data:
Precision = 0.8948
Recall=0.8279
Fscore=0.86

For Neg Data:
Precision = 0.8473
Recall=0.8911
Fscore=0.8688

**Using MegaM**

**SPAM Dataset**

For Spam Data:
Precision = 0.9553
Recall=0.9421
Fscore=0.9486

For HAM Data:
Precision = 0.9791
Recall=0.984
Fscore=0.9815

**SENTIMENT Dataset**

For Pos Data:
Precision = 0.8628
Recall=0.8375
Fscore=0.85

For Neg Data:
Precision = 0.8419
Recall=0.8666
Fscore=0.8541


# # **3.Part 3** # #

When only 10% of training data is used to train the model ,the results are as follows:
**# Part 1 # #**

The precision,recall and Fscore only decrease slightly by 0.05 approximately.As the model still has sufficient vocabulary size(known words) and same proportion of Spam/Ham documents,it still gives decent output.However if the new training has a different ratio of SPAM/HAM documents,the precision,recall and FScore of Ham documents , recall of Spam documents can decrease considerably because the prior probability information plays less role when there are almost same number of both documents.If the initial training data is very large(Million files),then using only 10 percent data for training won't affect the classification by much.

**# Part 2 #**

In part 2,the drop of precision,recall and Fscore is comparitively higher to Part1(~0.15-0.2). Both SVM and Megam seem to require large amount of training data to learn the model correctly.The number of features are greatly reduced when the size of the training set is reduced to only 10 percent,which results in poor performance in those off the shelf implementations.