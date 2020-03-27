import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

def load_iris(file_name):
    headers = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
    return pd.read_csv(file_name, names=headers)

def species_transform(iris):
    le = LabelEncoder()
    le.fit(iris["Species"])
    iris['Species'] = le.transform(iris['Species'])

def train_test_data_target_split(iris, test_size=0.3):
    train_set, test_set = train_test_split(iris, test_size=test_size)
    return train_set[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]].to_numpy(), train_set[["Species"]].to_numpy().ravel(), test_set[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]].to_numpy(), test_set[['Species']].to_numpy().ravel()

def getModel(trainData, trainTarget):
    classifier = GaussianNB()
    classifier.fit(trainData, trainTarget)
    return classifier

def test_accuracy(data, target):
    test_result = classifier.predict(test_data)
    error_count = (test_target != test_result).sum()
    return 1.0 - error_count/ target.shape[0]

if __name__ == '__main__':
    total_accuracy = 0
    for i in range(10):
        iris = load_iris('iris.data')
        species_transform(iris)
        train_data, train_target, test_data, test_target = train_test_data_target_split(iris, 0.3)
        classifier = getModel(train_data, train_target)
        total_accuracy += test_accuracy(test_data, test_target)
    print(total_accuracy)
