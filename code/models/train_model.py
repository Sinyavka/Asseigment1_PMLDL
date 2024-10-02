import joblib
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

wine = load_wine()
X = pd.DataFrame(data=wine['data'],columns=wine['feature_names'])
y = pd.DataFrame(data=wine['target'],columns=['target'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


joblib.dump(model, 'C:\\Users\\4734371\\Asseigment1_PMLDL\\models\\trained_model.pkl')
