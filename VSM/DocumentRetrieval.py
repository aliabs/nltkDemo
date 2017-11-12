from numpy import dot
from numpy.linalg import norm


def run(query_files, query_vector):
    v1 = query_files.values()
    v2 = query_vector.values()
    cosine = dot(v1, v2) / (norm(v1) * norm(v2))
    print("Similarity: %s", cosine)
    return cosine
