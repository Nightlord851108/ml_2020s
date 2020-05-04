'''
hw4 problem 2
'''
import pandas as pd
from sklearn.decomposition import FactorAnalysis
from sklearn.model_selection import train_test_split

HEADERS = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

def FA(dataset, headers, traget_dimension):
    converter = FactorAnalysis(n_components = target_dimension, random_state=0)
    data_value = dataset[headers[-1]]
    data_factors = dataset[headers[:-1]]
    fa_data = converter.fit_transform(data_factors.to_numpy())
    reduced_columns = ['nf{}'.format(str(i+1)) for i in range(traget_dimension)]
    result_data = pd.DataFrame(X_FA, columns=columns)
    result_data[headers[-1]] = data_value
    return result_data

if __name__ == '__main__':
    iris = pd.read_csv('iris.data', names=HEADERS)
    k = 5
    accuracies = []
    from pprint import pprint
    pprint(iris)
    for i in range(10):
        train_data, test_data = train_test_split(iris, test_size=0.3)
