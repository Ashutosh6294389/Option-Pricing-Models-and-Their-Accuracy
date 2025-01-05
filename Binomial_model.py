def binomial_model(S, K, T, r, sigma, N, option_type='call'):
    dt = T / N
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)

    # Initialize asset prices at maturity
    prices = [S * (u ** j) * (d ** (N - j)) for j in range(N + 1)]
    
    # Initialize option values at maturity
    if option_type == 'call':
        values = [max(price - K, 0) for price in prices]
    elif option_type == 'put':
        values = [max(K - price, 0) for price in prices]
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    # Backward induction
    for i in range(N - 1, -1, -1):
        values = [math.exp(-r * dt) * (p * values[j + 1] + (1 - p) * values[j]) for j in range(i + 1)]

    return values[0]

# Example usage
N = 50  # Number of time steps
print("Call Option Price:", binomial_model(S, K, T, r, sigma, N, 'call'))
print("Put Option Price:", binomial_model(S, K, T, r, sigma, N, 'put'))