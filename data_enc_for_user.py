import numpy as np


# Performed by Cloud Service Provider (CSP)
def convert_encrypted_data_for_user(encrypted_data, Mt):

    encrypted_data_for_user = []
    # print("In func convert_encrypted_data_for_user, encrypted_data: ", encrypted_data)

    # for row in encrypted_data:
        # Apply the transformation p′′i = p˜i * Mbase^(-1) * Mt^(-1)
        # encrypted_data_for_user.append(np.dot(row, np.linalg.inv(Mt)))
    # print("encrypted_data_for_user: ", encrypted_data_for_user)
    # print("Direct : ", np.dot(encrypted_data, np.linalg.inv(Mt)))

    encrypted_data_for_user = np.dot(encrypted_data, np.linalg.inv(Mt))
    return encrypted_data_for_user
