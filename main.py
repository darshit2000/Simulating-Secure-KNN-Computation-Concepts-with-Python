import numpy as np
from key_gen import key_generation
from data_enc import data_encryption
from query_enc import step1_query_encryption, step2_query_encryption, step3_query_decryption
from data_enc_for_user import convert_encrypted_data_for_user
from knn import compute_knn_encrypted_custom_k, compute_knn_unencrypted_custom_k
from data_dec import data_decryption

###########################################  Set Parameters #########################################################

n = 20              # number of vectors
d = 7               # dimension of vectors
c = 5               # length of the fixed vector w
epsilon = 4         # length of the fixed vector z
eta = d + 1 + c + epsilon
data_vectors = np.round(np.random.uniform(0, 20, size=(n, d)), 5)         # Database vectors
user_id = 1         # user id of the Query User
beta1 = 0.52        # encryption constant 1
beta2 = 0.84        # encryption constant 2
query_vector = np.round(np.random.uniform(0, 2000, size=d), 5)              # Query vector
k = 2               # KNN Parameter

#####################################################################################################################

print()
print("Database Matrix : ", np.round(data_vectors, 5))
print()
print("Query Vector : ", np.round(query_vector, 5))
print()

#####################################################################################################################

# Performed by Data Owner (DO)
Mbase, public_params, secret_key = key_generation(n, d, c, epsilon, eta)

#####################################################################################################################

# Performed by Data Owner (DO)
encrypted_data, Max_norm = data_encryption(data_vectors, secret_key, public_params)

#####################################################################################################################

# Performed by Query User (QU)
N, user_id, encrypted_query = step1_query_encryption(query_vector, user_id, beta1, d)

# Performed by Data Owner (DO)
Mt, doubly_encrypted_query = step2_query_encryption(encrypted_query, Max_norm, Mbase, c, epsilon, eta, beta2)

# Performed by Cloud Service Provider (CSP)
encrypted_data_for_user = convert_encrypted_data_for_user(encrypted_data, Mt)

# Perform by Query User (QU)
q_tilda_vector = step3_query_decryption(doubly_encrypted_query, d, N, eta)

#####################################################################################################################

# Cloud Service Provider (CSP) will run KNN
encrypted_output = compute_knn_encrypted_custom_k(q_tilda_vector, encrypted_data_for_user, user_id, k)

# Cloud Service Provider (CSP) will return the encrypted database vector, so we need to decrypt it
final_output = data_decryption(encrypted_output, Mt, Mbase, secret_key, d)

print("(Operation on encrypted data) Final Decrypted Output Vectors for k =", k , ": ", np.round(final_output,5))
print()
    
#####################################################################################################################

# For verification purpose, apply KNN computation on unencrypted data
# plain_output = compute_knn_unencrypted_custom_k(query_vector, data_vectors, user_id, k)

# print("(Operation on plain data) Final Decrypted Output Vectors for k =", k , ": ", np.round(plain_output,5))
# print()

#####################################################################################################################
