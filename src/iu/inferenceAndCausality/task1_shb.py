
'''
Created on 23.02.2025
Code for Workbook Inference & Causality Task1
@author: tillschoenbein
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, binom

def showByMeanAndKappa(mean_prior, kappa_prior, n_trials, n_successes):
# Parameters for the prior distribution (Beta distribution)


    a_prior, b_prior = calculate_beta_parameters(mean_prior, kappa_prior)
    print(f"Alpha (a): {a_prior}, Beta (b): {b_prior}")
    showByParameters(a_prior, b_prior, n_trials, n_successes)
    

def showByParameters(a_prior, b_prior, n_trials, n_successes):

    mean_prior = round(a_prior / (a_prior + b_prior),2)
    # Calculate the posterior distribution parameters
    a_post = a_prior + n_successes
    b_post = b_prior + (n_trials - n_successes)
    mean_post = round(a_post / (a_post + b_post),2)
    
    # Define the range for the x-axis (probability values)
    x = np.linspace(0, 1, 100)
    
    # Calculate the prior, likelihood, and posterior distributions
    prior_dist = beta.pdf(x, a_prior, b_prior)
    likelihood_dist = binom.pmf(n_successes, n_trials, x)
    posterior_dist = beta.pdf(x, a_post, b_post)
    
    # Plot the distributions
    plt.figure(figsize=(10, 6))
    plt.plot(x, prior_dist, label=f'Prior: Beta({a_prior}, {b_prior}), Mean≈{mean_prior}', color='blue')
    plt.plot(x, likelihood_dist, label=f'Likelihood: Binomial({n_successes}/{n_trials})', color='green')
    plt.plot(x, posterior_dist, label=f'Posterior: Beta({a_post}, {b_post}), Mean≈{mean_post}', color='red')
    plt.xlabel('Probability')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.show()

def calculate_beta_parameters(mean, kappa):
    """
    Calculate the parameters a and b of a Beta distribution given the mean.
    """    
    # Calculate alpha (a) and beta (b) using the mean and kappa
    alpha = mean * kappa
    beta = (1 - mean) * kappa
    
    return alpha, beta



# Example usage
mean_prior = 0.2
kappa_prior = 5

# Parameters for the likelihood function (Binomial distribution)
n_trials = 10
n_successes = 4


showByMeanAndKappa(mean_prior,5,n_trials,n_successes)
showByMeanAndKappa(mean_prior,100,n_trials,n_successes)