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