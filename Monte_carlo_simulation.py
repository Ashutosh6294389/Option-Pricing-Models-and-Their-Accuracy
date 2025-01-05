import numpy as np

def monte_carlo(S, K, T, r, sigma, simulations=100000, option_type='call'):
    dt = T
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

    if option_type == 'call':
        payoff = np.maximum(ST - K, 0)
    elif option_type == 'put':
        payoff = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    price = np.exp(-r * T) * np.mean(payoff)
    return price

# Example usage
print("Call Option Price:", monte_carlo(S, K, T, r, sigma, simulations=100000, option_type='call'))
print("Put Option Price:", monte_carlo(S, K, T, r, sigma, simulations=100000, option_type='put'))