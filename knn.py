from sklearn.neighbors import NearestNeighbors
import numpy as np
import sys

# Performed by Cloud Service Provider (CSP)
def compute_knn_encrypted_custom_k(q_tilda_vector, encrypted_data_for_user, user_id, k):
    data_mapper = {}
    for index,row in enumerate(encrypted_data_for_user):
        data_mapper[index] = np.dot(row, q_tilda_vector)
    # print("data-mapper dictionary: ", data_mapper)
    sorted_data_based_on_distance = sorted(data_mapper.items(), key=lambda x:x[1])
    minrows = []
    for i in range(k):
        minrows.append(encrypted_data_for_user[sorted_data_based_on_distance[i][0]])
        
    return minrows


# Performed by Cloud Service Provider (CSP)
def compute_knn_unencrypted_custom_k(query_vector, data_vector, user_id, k):
    data_mapper = {}
    for index,row in enumerate(data_vector):
        data_mapper[index] = np.linalg.norm(row - query_vector)
    # print("data-mapper dictionary: ", data_mapper)
    sorted_data_based_on_distance = sorted(data_mapper.items(), key=lambda x:x[1])
    minrows = []
    for i in range(k):
        minrows.append(data_vector[sorted_data_based_on_distance[i][0]])
        
    return minrows
