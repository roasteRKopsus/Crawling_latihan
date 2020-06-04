from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


from latihan_gabung import harga_count_bersih



y = harga_count_bersih['harga']
features = ['sum', 'terlaris', 'terbaru', 'relevansi']
X = harga_count_bersih[features]
print(X)


harga_model = DecisionTreeRegressor(random_state=1)
harga_model.fit(X, y)
harga_model.fit(X, y)
print(harga_model.predict(X.head()))
y.head()

y_hat = harga_model.predict(X)
print(mean_absolute_error(y, y_hat))

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
harga_model = DecisionTreeRegressor(random_state=1)
harga_model.fit(X_train, y_train)
print(harga_model.fit(X_train, y_train))

y_hat = harga_model.predict(X_test)
mean_absolute_error(y_test, y_hat)

print(mean_absolute_error(y_test, y_hat))

def get_mae(max_leaf_nodes, X_train, X_test, y_train, y_test):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(X_train, y_train)
    y_hat = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_hat)
    return mae


for max_leaf_nodes in [8,50,500,5000]:
    leaf_mae = get_mae(max_leaf_nodes, X_train, X_test, y_train, y_test)
    print(f'max leaf nodes: {max_leaf_nodes}\t mean absolute errror{int(leaf_mae)}')

rf_model = RandomForestRegressor(n_estimators=100, random_state=1)
rf_model.fit(X_train, y_train)
y_hat2 = rf_model.predict(X_test)
print(y_hat2)

print(f'MAE: {int(mean_absolute_error(y_test,y_hat))}')
