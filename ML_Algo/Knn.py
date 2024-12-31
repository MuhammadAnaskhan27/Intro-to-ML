from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing

# Selecting features and target
features = ['Age','Pclass','Fare']
target = 'Survived'

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(),inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(),inplace=True)

# Extract features and target 
x = titanic_df[features]
y = titanic_df[target]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 2. Model Initialization (Specific to KNN)
knn_model = KNeighborsClassifier(n_neighbors=5)  # DIFFERENT: Number of neighbors (k)

# 3. Model Training
knn_model.fit(X_train, y_train)

# 4. Predictions
y_pred = knn_model.predict(X_test)

# 5. Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
