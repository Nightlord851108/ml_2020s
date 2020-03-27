import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def load_iris(file_name):
    headers = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
    return pd.read_csv(file_name, names=headers)

def train_test_data_target_split(iris, test_size=0.3):
    train_x = iris[['SepalLength', 'SepalWidth', 'PetalLength']].values
    train_y = iris[['PetalWidth']].values
    return train_test_split(train_x, train_y, test_size=0.3)

def mse_test(regr, data, actual):
    predict_result = regr.predict(data)
    return mean_squared_error(actual, predict_result)

def train_model(iris, specy_name):
    iris_specy = iris.loc[iris['Species'] == specy_name]
    train_x, test_x, train_y, test_y = train_test_data_target_split(iris_specy, 0.3)
    regr = linear_model.LinearRegression()
    regr.fit(train_x, train_y)
    mse = mse_test(regr, test_x, test_y)
    return regr, mse

if __name__ == '__main__':
    iris = load_iris('iris.data')
    mse_dict = {
        'Iris-setosa': 0,
        'Iris-versicolor': 0,
        'Iris-virginica': 0
    }
    for i in range(10):
        setosa_model, mse = train_model(iris, 'Iris-setosa')
        mse_dict['Iris-setosa'] += mse
        versicolor_model, mse = train_model(iris, 'Iris-versicolor')
        mse_dict['Iris-versicolor'] += mse
        verginica_model, mse = train_model(iris, 'Iris-virginica')
        mse_dict['Iris-virginica'] += mse

    print('Iris-setosa model MSE: ' + str(mse_dict['Iris-setosa'] / 10))
    print('Iris-versicolor model MSE: ' + str(mse_dict['Iris-versicolor'] / 10))
    print('Iris-virginica model MSE: ' + str(mse_dict['Iris-virginica'] / 10))
