import cProfile
import pstats
from main import *

data = pd.read_csv('C:/Users/vali/Documents/Datasets/mnist_train.csv')
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]

profiler = cProfile.Profile()
profiler.enable()
w1, b1, w2, b2, acc = gradient_descent(X_train, Y_train, 0.1, 20)
profiler.disable()
print('-'*50+'\n')
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.print_stats()