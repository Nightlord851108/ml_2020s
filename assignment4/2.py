'''
hw4 problem 2
'''
import pandas as pd
from sklearn.decomposition import FactorAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

HEADERS = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

def FA(dataset, traget_dimension):
    converter = FactorAnalysis(n_components = target_dimension, random_state=0)
    fa_data = converter.fit_transform(dataset.to_numpy())
    reduced_columns = ['nf{}'.format(str(i+1)) for i in range(traget_dimension)]
    result_data = pd.DataFrame(X_FA, columns=columns)
    return result_data

if __name__ == '__main__':
    iris = pd.read_csv('iris.data', names=HEADERS)
    k = 5

    accuracies = []
    for i in range(10):
        train_data, test_data, train_ans, test_ans = train_test_split(iris[HEADERS[:-1]], iris[HEADERS[-1]], test_size=0.3)
        fa_train_data = FA(dataset=train_data, traget_dimension=3)
        fa_test_data = FA(dataset=test_data, traget_dimension=3)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(fa_train_datat , train_ans)
