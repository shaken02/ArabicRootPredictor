#  Load Model and Vectorizer
model = joblib.load('arabic_root_predictor.pkl')

vectorizer = joblib.load('arabic_tfidf_vectorizer.pkl')

print("Successfuly loaded")

# Type your word
new_data = ["كتبت"]  

# Vectorize this word
new_data_vec = vectorizer.transform(new_data)

# Predict the root of chosen word
prediction = model.predict(new_data_vec)
print(prediction[0])
