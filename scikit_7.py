from sklearn.feature_extraction.text import CountVectorizer
import bucket

vectorizer = CountVectorizer()
corpus_norwa = bucket.f_norwa_list
X = vectorizer.fit_transform(corpus_norwa)
print(X)

vectorizer.get_feature_names_out()

print(X.toarray())

vectorizer.vocabulary_.get('document')