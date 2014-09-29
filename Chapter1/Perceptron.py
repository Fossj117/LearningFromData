"""
Answer for Exercise 1.4 
"""

import numpy as np
import matplotlib.pyplot as plt

class Perceptron(object): 
    

    def __init__(self, dim=2, N=20, bounds=(-10, 10)):
        """
        Initialize the perceptron learning situation

        INPUT: 
            dim : int, dimensionality of the perceptron (e.g. 2)
            N : int, size of the data set. 
            bounds : (int, int) tuple giving bounds of data generation
        """

        self.dim = dim # number of dimensions
        self.N = N # number of observations
        self.lb, self.ub = bounds

        # generate the data. 
        self.true_w, self.data, self.true_labels = self.generate_training_data()


    def generate_training_data(self):
        """
        Randomly generates linearly separable training data for the perceptron algorithm. 

        OUTPUT: 
            true_w : np array of size (dim+1,), the true values of the sep. hyperplane
            data : np array of shape (N, dim+1), the randomly generated data
            labels : the true label values of the data.
        """

        # randomly choose true_w
        true_w = np.random.uniform(self.lb, self.ub, self.dim+1)

        ### Generate the data. 
        ones = np.ones(self.N).reshape(self.N, 1)
        raw_data = np.random.uniform(self.lb, self.ub, (self.N, self.dim))

        # full data with intercept term included
        data = np.concatenate([ones, raw_data], axis=1)

        # get true labels.
        labels = self.activate(true_w, data)

        return true_w, data, labels


    def activate(self, w, data):
        """
        INPUT: 
            w : numpy array of shape (dim+1,)
            data : np array of shape (N, dim+1)
        OUTPUT: 
            np array w/ values +1 or -1 as selected by perceptron with
            the given value of w. 
        """

        dots = data*w
        return np.array([1 if act > 0 else -1 for act in dots.sum(axis=1)])


    def train(self, labels):
        """
        Run the perceptron learning algorithm
        """

        # randomly initialize the w value. 
        w = np.random.uniform(self.lb, self.ub, dim+1)

        current_labels = self.activate(w, self.data)
        true_labels = labels

        while not all(current_labels = true_labels):
        # while haven't yet converged

            # indices that are currently missed
            missed_inds = np.where(current_labels != true_labels)

            # choose a random missed index
            chosen_ind = np.random.choice(missed_inds, 1)

    def plot(self):
        """
        Plot myself.... 
        """
        pass





