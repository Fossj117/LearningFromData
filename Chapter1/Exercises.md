### Chapter 1 Exercises

**(1.1)**

* Medical diagnosis: 
	* **Input space**: variables about relevant features of medical history; variables about presence/absence or intensity of relevant symptoms
	* **Output space**: {has disease, doesn't have disease} or multiclass depending on situation
	* **Target Function**: Mapping from symptom/med history variables to disease labels. 
	* **Dataset**: Historical data about patients, including their symptoms, medical histories and their ultimate diagnoses. 
* Handwritten digit recognition: 
	* **Input space**: Standardized-images of the digits, encoded as pixel intensity values, or perhaps some higher-level derived variables (e.g. symmetry)
	* **Output space**: {0 - 9}
	* **Target Function**: Maps pixel values to a digit label
	* **Dataset**: Encoded images of handwritten digits with (hand-coded) labels. 
* Spam Detection: 
	* **Input space**: (vectorized) raw text of spam and ham messages (e.g. based on possibly-restricted bag of words)
	* **Output space**: {'spam', 'ham'} labels
	* **Target Function**: mapping from word presence/absences to labelings
	* **Dataset**: sample of spam and ham messages
* Medical diagnosis: 
	* **Input space**: variables about relevant features of medical history; variables about presence/absence or intensity of relevant symptoms
	* **Output space**:
	* **Target Function**:
	* **Dataset**:

**(1.2)**: 

* Large positive weights: "FREE", "VIAGRA", "BUY", "JOIN", etc. 
* Long, complicated words that never appear in spam messages. 
* The bias term, *b*

**(1.3)**

See written work

**(1.4)**

See `Perceptron.py` script. 

**(1.5)**

Which of the following problems are more sutied for the learning approach and which are more suited for the design approach?

* Learning approach: a, c, e
* Design approach: b, d

**(1.6)**

a. Supervised

b. Reinforcement

c. Supervised if you have labels, otherwise unsupervised

d. Reinforcement?

  e. Supervised…?

**(1.7)**

Amount of agreement: number of f's  

(a) 

* 3: 1
* 2: 3
* 1: 3
* 0: 1

(b)

* 3: 1
* 2: 3
* 1: 3
* 0: 1

©

* 3: 1
* 2: 3
* 1: 3
* 0: 1

(d) Not going to actually do this one, but easy to prove that it will have the same distribution as all of the others. 

Why? 

Algo picks some pattern, given the training set: (d1, d2, d3). In the test set, we have all possible unique three digit binary combos. How many agree on all three? Only one: d1, d2, d3. How many disagree on all three? Only one: ~d1, ~d2, ~d3. How many agree on 2 out of 3? 3 choose 1 = 3. How many agree on 1 out of 3? 3 choose 2 = 3. 

**(1.8)**

In R:

```
> (0.1)^10 + 10*(0.9)*(0.1^9)
[1] 9.1e-09
```

or: 

```
> pbinom(1, 10, 0.9) 
[1] 9.1e-09
```

**(1.9)**

```
In [9]: import numpy as np

In [10]: def Hoeffding_Bound(eps, N):
    return 2*np.exp(-2*(eps**2)*N)
   ....: 

In [11]: Hoeffding_Bound(eps=0.9-0.1, N=10)
Out[11]: 5.521545144074388e-06
```

So Hoeffding bound is larger than the true probability for this particular case. I.e. it is not a very "tight" bound on the probability that `u` and `v` differ by the given amount (in this case)






