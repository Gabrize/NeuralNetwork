from LABS.FirstLab.E_Flatness_Classificator_Data import load_data_func
from keras import Sequential, callbacks
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np

import ADDITIONAL.GUI_REPORTER as gr

if __name__ == '__main__':
    train_size = 100
    (x_train, y_train), (x_test, y_test) = load_data_func(train_size, show=True, k=1, b=0, func_type='n_lin')

    first_layer_nur = 1
    lr = 0.3
    batch_size = 10
    epochs = 10
    verbose = 1

    model = Sequential()

    model.add(Dense(first_layer_nur, input_dim=1, kernel_initializer='glorot_normal', activation='linear'))
    model.compile(loss='mean_squared_error', optimizer=SGD(lr=lr), metrics=['mae'])

    # batch_size define speed of studying
    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=verbose)

    score = model.evaluate(x_test, y_test, verbose=verbose)

    print("\nabsolute_error on train data\t %.f%%" % (history.history['mean_absolute_error'][epochs - 1] * 100))
    print("\nabsolute_error on testing data %.f%%" % (score[1] * 100))
    print("loss on train data %.f%%" % (history.history['loss'][epochs - 1] * 100))
    gr.plot_history_separte(history=history, acc='mean_absolute_error',
                            save_path_acc="ACC.png", save_path_loss="LOSS.png",
                            save=True, show=True)

    plt.plot(np.append(x_train,x_test), model.predict(np.append(x_train,x_test)), '.')
    plt.plot(np.append(x_train,x_test), np.append(y_train,y_test), '.')

    plt.legend(('approximation','function'), loc='upper left', shadow=True)

    plt.show()
    plt.close()

    h = 0.05
    count = 0

    for rate in np.arange(lr, 1.0, h, dtype=float):
        print("\nrate = ", rate)
        loc_loss = history.history['loss'][epochs - 1]
        lr = rate
        model = Sequential()

        model.add(Dense(first_layer_nur, input_dim=1, kernel_initializer='glorot_normal', activation='linear'))

        model.compile(loss='mean_squared_error', optimizer=SGD(lr=lr), metrics=['mae'])

        # batch_size define speed of studying
        history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=0)

        score = model.evaluate(x_test, y_test, verbose=0)

        print("loss on train data %.f%%" % (history.history['loss'][epochs - 1] * 100))

        if history.history['loss'][epochs - 1] - loc_loss >= 0.01:
            break
    lr -= h

    titles = np.array(['lower than max', 'max', 'higher than max'])
    tit_cont = 0

    step = 0.05

    for j in np.arange(lr - 3 * step, lr + 4 * step, 3 * step, dtype=float):

        model = Sequential()

        weights_arr = np.array([[2.0]], dtype=float)
        bias_arr = np.array([-0.25], dtype=float)
        x_range = np.array([1])

        model.add(Dense(first_layer_nur, input_dim=1, weights=list([weights_arr, bias_arr]), activation='linear'))

        model.compile(loss='mean_squared_error', optimizer=SGD(lr=j), metrics=['mae'])

        for i in np.arange(1, epochs, 1, dtype=float):
            model.fit(x_train, y_train, batch_size=batch_size, epochs=1, verbose=0)
            weights_arr = np.append(weights_arr, model.get_weights()[0])
            bias_arr = np.append(bias_arr, model.get_weights()[1])
            x_range = np.append(x_range, i)

        plt.plot(x_range, weights_arr, '.')
        plt.plot(x_range, bias_arr, '.')
        plt.title('learning rate = %-0.2f %s' % (j, titles[tit_cont]))
        plt.legend(('weights', 'biases'), loc='upper left', shadow=True)

        plt.show()
        plt.close()
        tit_cont += 1
