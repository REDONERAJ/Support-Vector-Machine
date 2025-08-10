import joblib
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='rbf', C=1, gamma='scale', probability=True)
model.fit(X_train, y_train)

joblib.dump((model, iris.target_names), "svm_iris_model.pkl")
