Option Pricing Models and Their Accuracy

Objective

The primary goal of this project is to implement and evaluate popular option pricing models such as Black-Scholes, Binomial Tree, and Monte Carlo Simulation to predict derivative prices accurately and assess their performance using real-world and simulated data.

Features

Mathematical implementation of the Black-Scholes, Binomial Tree, and Monte Carlo models for option pricing.
Comparative analysis of model efficiency and accuracy using historical and simulated data.
Visualization of results for better interpretation and decision-making.
Setup Instructions

Clone the Repository:
  git clone <repository_url>
  cd <repository_name>
  Install Dependencies: Ensure you have Python 3.7+ installed. Install the required packages using:
  pip install -r requirements.txt


Dependencies:

 numpy 
 scipy
 matplotlib
 yfinance (for fetching historical data)
 Run the Code: Execute the Python files to test each model:
 python black_scholes.py
 python binomial_model.py
 python monte_carlo.py
 Usage

Black-Scholes Model
Calculate European option prices using closed-form equations:

from black_scholes import black_scholes

price = black_scholes(S=100, K=110, T=1, r=0.05, sigma=0.2, option_type='call')
print("Call Option Price:", price)
Binomial Tree Model
Simulate step-wise price evolution for European and American options:

from binomial_model import binomial_model

price = binomial_model(S=100, K=110, T=1, r=0.05, sigma=0.2, N=50, option_type='call')
print("Call Option Price:", price)
Monte Carlo Simulation
Generate probabilistic forecasts for option prices:

from monte_carlo import monte_carlo

price = monte_carlo(S=100, K=110, T=1, r=0.05, sigma=0.2, simulations=100000, option_type='call')
print("Call Option Price:", price)
Project Workflow

Phase 1: Research
Gain a theoretical understanding of derivatives and pricing models.
Explore real-world data from financial APIs like Yahoo Finance.
Phase 2: Development
Implement the mathematical formulas for Black-Scholes, Binomial, and Monte Carlo models in Python.
Test model implementations on historical and simulated data.
Phase 3: Analysis and Visualization
Apply models to identical datasets and evaluate results.
Use metrics like Mean Absolute Error (MAE) to measure accuracy.
Visualize results through charts (e.g., predicted vs. actual prices, runtime comparisons).
Visualization

Accuracy Analysis: Compare model predictions to actual market prices.
Efficiency Analysis: Evaluate runtime and computational overhead for each model.
Graphs: Use matplotlib to generate visual insights.
Expected Outcomes

Model Accuracy: Assess the precision of each pricing model in predicting market prices.
Computational Efficiency: Determine runtime and resource consumption.
Practical Insights: Highlight strengths and weaknesses of each model for real-world applications.