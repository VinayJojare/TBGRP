# Sample code for cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
from plagiarism_detector_project.plagiarism_detector_app.feature_extraction import tfidf_matrix

cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
print(cosine_sim[0][0])
