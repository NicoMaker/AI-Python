import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Caricamento del dataset
csv = pd.read_csv("Employee_Salaries.csv")

# Seleziona le colonne di interesse
features = ['Base_Salary', 'Overtime_Pay', 'Longevity_Pay','Gender']
target = 'Department_Name'

# Split dei dati in training set e test set
X = csv[features]
y = csv[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Creazione di un trasformatore per la codifica one-hot della feature 'Gender'
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['Gender'])
    ],
    remainder='passthrough'
)

# Creazione del pipeline con normalizzazione e addestramento del perceptron
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('scaler', StandardScaler()),
    ('perceptron', Perceptron(max_iter=1000, tol=0.001, eta0=0.01, random_state=1))
])

# Addestramento del modello
pipeline.fit(X_train, y_train)

# Valutazione delle prestazioni del modello sul test set
accuracy = pipeline.score(X_test, y_test)
print("Accuratezza: ", accuracy)

# Esempio di predizione con nuovi dati
new_example = pd.DataFrame([[145613.36,0,0,'M'
]], columns=features)
predicted_class = pipeline.predict(new_example)
print("Classe Predetta: ", predicted_class)