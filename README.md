# Simulating-Secure-KNN-Computation-Concepts-with-Python

In order to reduce the strain on local storage and computer resources, cloud computing has become popular as a trend of outsourcing database and query services to a strong cloud. Nevertheless, there is a chance that secret and private data will be compromised while using cloud computing and private data storage. As a result, before being stored in the cloud, important apps must first be encrypted. Additionally, the data must be in the encrypted domain’s computation-friendly ciphertext form in order to run various data mining methods, such as k-NN. Data is therefore encrypted before being outsourced to the cloud using a searchable encryption algorithm.

In this project, I have implemented secure KNN algorithm that can be directly performed on the encrypted data on the cloud and I have used Asymmetric Scalar- product-Preserving Encryption (ASPE) to implement the key-generation, data encryption, query encryption, and secure KNN. By lowering the query encryption time using ASPE, the encryption strategy becomes more practical and efficient. Additionally, it aids in achieving query secrecy and data privacy.

-----------------

# WORKFLOW OF THIS IMPLEMENTATION

The security model of secure k-NN computation consists of three entities: a data owner (DO), a cloud service provider (CSP), and a group of query users (QU). The Query User (QU) wants to query the database that is sent by the Data Owner (DO) to the Cloud Service Provider (CSP). But we want to do this in an encrypted version. The following steps specifies the workflow of this algorithm:

(1)	First, DO will generate its secret key using the key generation function. Then DO uses a searchable encryption algorithm similar to the function data encryption to encrypt its database before storing it in the cloud.

(2)	A QU encrypts its query vector using the encryption algorithm step1 query encryption with the intention of computing the k-NN of its query vector and then will send this encrypted query to Data Owner (DO) for query re-encryption by the DO’s secret key.

(3)	When DO receives the query vector from a QU, it uses the step2 query encryption procedure to re-encrypt it before sending it back to the QU.

(4)	As stated in the function step3 query decryption, QU removes its encryption layer upon receiving a doubly encrypted query vector from the DO and forwards the encrypted query vector to the CSP for k-NN computation.

(5)	CSP verifies the user ID and calculates k-NN using the relevant data as shown in the function compute knn encrypted custom k. The de- rived k-NN solution is then sent to the QU. But this solution is currently encrypted.

(6)	data decryption procedure is used to decrypt the encrypted data vectors that we got from the procedure compute knn encrypted custom k

------------------

# Instruction for running the code

All helper files are been included in the main.py.  So, we only need to run “python3 main.py”.

----------------

# References

Secure KNN Computation On Cloud by Tikaram Sanyashi, Nirmal Kumar Boran, and Virendra Singh

