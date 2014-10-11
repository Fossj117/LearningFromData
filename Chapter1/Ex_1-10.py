"""
Exercise 1.10: 

(a) What is mu for the three coins selected? 0.5 

(b) Repeat the experiment a large number of times to get several instances of v_1, 
v_rand and v_min and plot the histograms of the distributions of v_1, v_rand and v_min.
Notice that which coins end up being c_rand and c_min may differ from one run to another. 

"""

import numpy as np
import pandas as pd

def flip_coin(prob=0.5, n_flips=10): 
	""" 
	Flip a coin n_flips times 

	Return:
	 - an array of 1's and 0's of shape n_flips, and 
	 - the fraction of heads (i.e. v for this trial)
	"""

	flip_results = (np.random.rand(n_flips) > prob)*1

	return flip_results, flip_results.mean()


def run_experiment(n_coins=1000):
	"""
	Flip 1000 coins ten times each. Return: 

	- v_1 : fraction of heads for first coin flipped
	- v_rand : fraction of heads for a random coin
	- v_min : fraction of head for the coin with *least* heads
	"""

	flips = [flip_coin() for _ in xrange(0,n_coins)]

	v_1 = flips[0][1]
	v_rand = flips[np.random.randint(low=0, high=n_coins-1)][1]
	v_min = min([v for _, v in flips])

	return {"v_1":v_1, "v_rand":v_rand, "v_min":v_min}

if __name__ == "__main__":

	# Part (b)	
	experiments = [run_experiment() for _ in xrange(0,100)]
	results_df = pd.DataFrame(experiments)

	results_df.v_1.hist(n_bins=9)
	results_df.v_rand.hist(n_bins=9)
	results_df.v_min.hist(n_bins=9)






