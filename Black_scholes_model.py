import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return price

# Example usage
S = 100  # Current stock price
K = 110  # Strike price
T = 1    # Time to maturity (in years)
r = 0.05 # Risk-free rate
sigma = 0.2 # Volatility

print("Call Option Price:", black_scholes(S, K, T, r, sigma, 'call'))
print("Put Option Price:", black_scholes(S, K, T, r, sigma, 'put'))