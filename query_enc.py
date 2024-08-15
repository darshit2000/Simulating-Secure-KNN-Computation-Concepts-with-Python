import numpy as np

# Performed by Query User (QU)
def step1_query_encryption(query_vector, user_id, beta1, d):
    
    # Generate a diagonal matrix N(d×d) of real numbers
    N = np.diag(np.round(np.random.uniform(0, 2000, size=d), 5))
    # print("N(dxd): ", N)

    # Compute the encrypted query q˙
    encrypted_query = beta1 * np.dot(query_vector, N)

    # Return the encrypted query along with user id
    return N, user_id, encrypted_query


# Performed by Data Owner (DO)
def step2_query_encryption(encrypted_query, Max_norm, Mbase, c, epsilon, eta, beta2):
    
    # Compute the largest number present in the encrypted query vector q˙
    qmax = np.max(encrypted_query)
    # print("qmax: ", qmax)

    # Sample a temporary secret matrix Mt(η×η)
    # Mt = 2000 * np.random.rand(eta, eta)
    Mt = np.round(np.random.uniform(0, 2000, size=(eta, eta)), 5)
    
    # Ensure that the diagonal elements are larger than Max_norm
    Mt[np.diag_indices(eta)] = np.random.uniform(Max_norm, 2000 * Max_norm, eta)

    # Ensure that all elements except diagonal are larger than qmax
    for i in range(eta):
        for j in range(eta):
            if i != j:
                Mt[i, j] = np.random.uniform(qmax, 2000 * qmax)

    # print("Mt: ", Mt)
    
    # Multiply matrix Mt with Mbase to obtain a temporary secret matrix Msec
    Msec = np.dot(Mt, Mbase)

    x = np.random.randint(0, 2000, c)  
    # print("x: ", x)
    
    zero_vector_epsilon = np.zeros(epsilon)
    # print("zero_vector_epsilon: ", zero_vector_epsilon)
    
    # Append query vector q˙ to obtain a new query vector q′ of η-dimension
    new_query_vector = np.concatenate([encrypted_query, [1], x, zero_vector_epsilon])
    # print("new_query_vector: ", new_query_vector)

    q_eta_eta = np.diag(new_query_vector)
    # print("q_eta_eta: ", q_eta_eta)

    # Sample elements of the error matrix E uniformly at random larger than qmax
    # E = np.random.uniform(qmax, 2000 * qmax, (eta, eta))
    E = np.round(np.random.uniform(qmax, 2000 * qmax, size=(eta, eta)), 5)
    # print("Error Matrix: ", E)

    # Compute the doubly encrypted query vector qˆ
    doubly_encrypted_query = beta2 * (np.dot(Msec, q_eta_eta) + E)

    return Mt, doubly_encrypted_query


# Performed by Query User (QU)
def step3_query_decryption(doubly_encrypted_query, d, N, eta):
    
    # print("N: ", N)
    # Construct a diagonal matrix N'η×η with first d diagonal elements same as that of the matrix N(d×d)
    N_prime = np.round(np.diag(np.concatenate([np.diag(N), np.ones(eta-d)])), 5)
    # print("N prime: ", N_prime)

    # Compute the inverse of N'
    inverse_N_prime = np.linalg.inv(N_prime)

    # Remove the encryption layer to obtain q˜enc
    q_tilda_matrix = np.dot(doubly_encrypted_query, inverse_N_prime)
    # print("q_tilda_matrix: ", q_tilda_matrix)
    
    # q_tilda_vector = []
    # [q_tilda_vector.append(np.sum(row)) for row in decrypted_query]
    q_tilda_vector = np.sum(q_tilda_matrix, axis=1)
    # print("q_tilda_vector: ", q_tilda_vector)
    
    return q_tilda_vector


