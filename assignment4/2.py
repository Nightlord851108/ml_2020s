'''
hw4 problem 2
'''
import pandas as pd
from sklearn import metrics
from sklearn.decomposition import FactorAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

HEADERS = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

def FA(dataset, target_dimension):
    converter = FactorAnalysis(n_components = target_dimension, random_state=0)
    fa_data = converter.fit_transform(dataset.to_numpy())
    reduced_columns = ['nf{}'.format(str(i+1)) for i in range(target_dimension)]
    result_data = pd.DataFrame(fa_data, columns=reduced_columns)
    return result_data

def average(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':
    iris = pd.read_csv('iris.data', names=HEADERS)
    k = 5

    accuracies = []
    for i in range(10):
        train_data, test_data, train_ans, test_ans = train_test_split(iris[HEADERS[:-1]], iris[HEADERS[-1]], test_size=0.3)
        fa_train_data = FA(train_data, 3)
        fa_test_data = FA(test_data, 3)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(fa_train_data, train_ans)
        test_predict = knn.predict(fa_test_data)
        acc = metrics.accuracy_score(test_ans, test_predict)
        print("\rK: {}, i= {}: {:.2%}".format(k, i, acc))
        accuracies.append(acc)
    print('-----------------')
    print("Average: {:.2%}".format(average(accuracies)))
