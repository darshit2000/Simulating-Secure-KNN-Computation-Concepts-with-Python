import numpy as np

# Performed by Data Owner (DO)
def data_encryption(data_vectors, secret_key, public_params):
    s = secret_key['s']
    Mbase = secret_key['Mbase']
    w = secret_key['w']
    epsilon = public_params['epsilon']

    # Initialize encrypted data vectors
    encrypted_data = []
    
    # Sample ephemeral secret vector z of size epsilon
    # z = 2000 * np.random.rand(epsilon)
    z = np.round(np.random.uniform(0, 2000, size=epsilon), 5)
          
    # Initialize Max_norm
    Max_norm = 0

    for i in range(len(data_vectors)):
        pi = data_vectors[i]

        # Pre-process data vector into p~i
        preprocessed_vector = np.concatenate([
            s[:-1] - 2 * pi[:],
            np.array([s[-1] + np.linalg.norm(pi)**2]),
            w,
            z
        ])                                                          
        
        # Encrypt data vector using vector-matrix multiplication
        pi_dash = np.dot(preprocessed_vector, np.linalg.inv(Mbase))     # pi'

        # Update Max_norm
        norm_pi = np.linalg.norm(pi)
        Max_norm = max(Max_norm, norm_pi)

        encrypted_data.append(pi_dash)

    return encrypted_data, Max_norm


