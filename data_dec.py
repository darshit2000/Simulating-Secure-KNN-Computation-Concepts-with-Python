import numpy as np


def data_decryption(encrypted_output, Mt, Mbase, secret_key, d):
    result_list = []
    
    for row in encrypted_output:
        # Get pi~ from pi''
        pi_tilda = np.dot(np.dot(row, Mt), Mbase)
        # print("pi_tilda: ", pi_tilda)
        
        #dimension of s is d+1
        secret_key_s = secret_key['s']
        
        output_pi = []
        for index,val in enumerate(pi_tilda):
            # create pi of dimension d
            if index < d:
                output_pi.append((secret_key_s[index] - val)/2)
            else:
                break
        result_list.append(output_pi)     
        # print("result_list: ", result_list)
        
    return result_list