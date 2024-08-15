import numpy as np

# Performed by Data Owner (DO)
def key_generation(n, d, c, epsilon, eta):

    # Sample base secret matrix Mbase
    # Mbase = 2000 * np.random.rand(int(eta), int(eta))
    Mbase = np.round(np.random.uniform(0, 2000, size=(eta, eta)), 5)
    # print("Mbase: ", Mbase)

    # Generate long-term secret vector s of size d+1
    # s = 2000 * np.random.rand(d + 1)
    s = np.round(np.random.uniform(0, 2000, size=(d+1)), 5)
    # print("s: ", s)

    # Generate fixed vector w for each data vector of size c
    # w = 2000 * np.random.rand(c)
    w = np.round(np.random.uniform(0, 2000, size=c), 5)
    # print("w: ", w)

    # Construct public parameters c and epsilon
    public_params = {'c': c, 'epsilon': epsilon}

    # Secret key
    secret_key = {'s': s, 'Mbase': Mbase, 'w': w}

    return Mbase, public_params, secret_key

