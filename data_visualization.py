import matplotlib.pyplot as plt

def plot_data(df):
    df.hist(figsize=(10, 10))
    plt.show()

def plot_predictions(model, X_test, y_test):
    predictions = model.predict(X_test)
    plt.scatter(y_test, predictions)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.show()
