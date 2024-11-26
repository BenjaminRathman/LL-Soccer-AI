#splitting into training and testing
from sklearn.tree import DecisionTreeClassifier # type: ignore
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # type: ignore
import pandas as pd # type: ignore
#from sklearn.datasets import load_wine # type: ignore

     

data = []
df = pd.DataFrame(data["data"], columns=data.feature_names)
df["target"] = data.target
df.head()


X = df.drop(columns="target")
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y)
     


#from sklearn.tree import DecisionTreeClassifier, plot_tree
#import matplotlib.pyplot as plt

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
X_train.loc[0, "flavanoids"]

model.score(X_test, y_test)
     