from sklearn.neighbors import KNeighborsClassifier

class KNN:

    def __init__(self, k, X_train, y_train):
        self.k = k
        self.X_train = X_train
        self.y_train = y_train
        self.distance_matrix = None
    
    def train(self):
        knn = KNeighborsClassifier(n_neighbors=self.k)
        self.distance_matrix = knn.fit(self.X_train, self.y_train)


    def predict(self, example):
        y_pred = self.distance_matrix.predict(example)
        return y_pred

    def get_error(self, predicted, actual):
        return sum(map(lambda x : 1 if (x[0] != x[1]) else 0, zip(predicted, actual))) / len(predicted)

    def test(self, test_input, labels):
        actual = labels
        predicted = (self.predict(test_input))
        print("error = ", self.get_error(predicted, actual))

# Add the dataset here

from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

# train, test = train_test_split(iris, test_size=0.2)
# Split the data 70:30 and predict.
plt.boxplot(X)
#plt.show()
nbs = 3
object = KNN(nbs, X_train, y_train)
# create a new object of class KNN

# plot a boxplot that is grouped by Species. 
# You may have to ignore the ID column

# predict the labels using KNN
object.train()
print(object.predict(X))
# use the test function to compute the error
object.test(X_test, y_test)
