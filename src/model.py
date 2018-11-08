from keras.models import Sequential
from keras.models import Model

from keras.layers import Input
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Bidirectional
from keras.layers import Dropout
from keras.layers import Conv1D
from keras.layers import MaxPooling1D
from keras.layers import UpSampling1D
from keras.layers import Concatenate

from keras.optimizers import Adam


def simple_LSTM():
    np.random.seed(99)
    model = Sequential(name='simple_LSTM')
    model.add(LSTM(512, input_shape=(None, 6), recurrent_dropout=0.5))
    model.add(Dense(len(activities), activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=Adam(
        lr=1e-3), metrics=['accuracy', 'mse', f1])
    print(model.summary())
    return model


def bidirectional_LSTM():
    np.random.seed(7)
    model = Sequential(name='bidirectional_LSTM')
    model.add(Bidirectional(LSTM(50), input_shape=(
        None, 6), recurrent_dropout=0.5))
    model.add(Dense(len(activities), activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=Adam(
        lr=1e-3), metrics=['accuracy', 'mse', f1])
    print(model.summary())
    return model


def conv_LSTM():
    # Create the model
    np.random.seed(7)
    optimizer = Adam(lr=1e-4, decay=1e-6, clipnorm=0.6)
    model = Sequential(name='conv_LSTM')
    model.add(Conv1D(128,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1,
                     input_shape=(180, 6)))
    model.add(Conv1D(64,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1))
    # model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(64,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1))
    model.add(Conv1D(64,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1))
    model.add(LSTM(256, return_sequences=True,
                   dropout=0.2, recurrent_dropout=0.2))
    model.add(LSTM(256, return_sequences=True,
                   dropout=0.2, recurrent_dropout=0.2))
    model.add(Flatten())
    #model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(len(activities), activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer, metrics=['accuracy'])
    print(model.summary())
    return model


def conv_LSTM():
    # Create the model
    np.random.seed(7)
    optimizer = Adam(lr=1e-4, decay=1e-6, clipnorm=0.6)
    model = Sequential(name='conv_LSTM')
    model.add(Conv1D(128,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1,
                     input_shape=(180, 6)))
    model.add(Conv1D(64,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1))
    # model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(64,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1))
    model.add(Conv1D(64,
                     4,
                     padding='valid',
                     activation='relu',
                     strides=1))
    model.add(LSTM(256, return_sequences=True,
                   dropout=0.2, recurrent_dropout=0.2))
    model.add(LSTM(256, return_sequences=True,
                   dropout=0.2, recurrent_dropout=0.2))
    model.add(Flatten())
    #model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(len(activities), activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer, metrics=['accuracy'])
    print(model.summary())
    return model


def conv_LSTM2():
    # Create the model
    np.random.seed(7)
    optimizer = Adam(lr=1e-4)
    model = Sequential(name='conv_LSTM2')
    model.add(Conv1D(16,
                     3,
                     padding='same',
                     activation='relu',
                     strides=1,
                     kernel_initializer='glorot_uniform',
                     input_shape=(180, 6)))
    model.add(Conv1D(32,
                     3,
                     padding='same',
                     activation='relu',
                     strides=1,
                     kernel_initializer='glorot_uniform'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(64,
                     3,
                     padding='same',
                     activation='relu',
                     strides=1,
                     kernel_initializer='glorot_uniform'))
    model.add(Conv1D(128,
                     3,
                     padding='same',
                     activation='relu',
                     strides=1,
                     kernel_initializer='glorot_uniform'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(LSTM(256, return_sequences=True,
                   dropout=0.5, recurrent_dropout=0.5))
    model.add(LSTM(512, return_sequences=True,
                   dropout=0.5, recurrent_dropout=0.5))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(len(activities), activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer, metrics=['accuracy'])
    print(model.summary())
    return model


def UNet_LSTM():
    optimizer = Adam(lr=1e-4)
    inputs = Input((180, 6))

  # encoding phase
    conv1 = Conv1D(32,
                   3,
                   padding='same',
                   activation='relu',
                   strides=1,
                   kernel_initializer='glorot_uniform')(inputs)
    conv2 = Conv1D(32,
                   3,
                   padding='same',
                   activation='relu',
                   strides=1,
                   kernel_initializer='glorot_uniform')(conv1)
    pool1 = MaxPooling1D(pool_size=2)(conv2)  # 90

    conv3 = Conv1D(64,
                   3,
                   padding='same',
                   activation='relu',
                   strides=1,
                   kernel_initializer='glorot_uniform')(pool1)
    conv4 = Conv1D(64,
                   3,
                   padding='same',
                   activation='relu',
                   strides=1,
                   kernel_initializer='glorot_uniform')(conv3)
    pool2 = MaxPooling1D(pool_size=2)(conv4)  # 45

    #   conv5 = Conv1D(128,
    #                  3,
    #                  padding='same',
    #                  activation='relu',
    #                  strides=1,
    #                  kernel_initializer = 'glorot_uniform')(pool2)
    #   conv6 = Conv1D(128,
    #                  3,
    #                  padding='same',
    #                  activation='relu',
    #                  strides=1,
    #                  kernel_initializer = 'glorot_uniform')(conv5)
    #   pool3 = MaxPooling1D(pool_size = 2)(conv6) #

    # middle phase
    conv7 = Conv1D(128,
                   3,
                   padding='same',
                   activation='relu',
                   strides=1,
                   kernel_initializer='glorot_uniform')(pool2)
    conv8 = Conv1D(128,
                   3,
                   padding='same',
                   activation='relu',
                   strides=1,
                   kernel_initializer='glorot_uniform')(conv7)
    drop1 = Dropout(0.5)(conv8)

    # decoding phase
    #   up1 = Conv1D(128,
    #                  2,
    #                  padding='same',
    #                  activation='relu',
    #                  strides=1,
    #                  kernel_initializer = 'glorot_uniform')(UpSampling1D(size = 2)(drop1))
    #   concat1 = Concatenate(axis=-1)([conv6, up1])
    #   conv9 = Conv1D(128,
    #                  3,
    #                  padding='same',
    #                  activation='relu',
    #                  strides=1,
    #                  kernel_initializer = 'glorot_uniform')(UpSampling1D(size = 2)(concat1))
    #   conv10 = Conv1D(128,
    #                  3,
    #                  padding='same',
    #                  activation='relu',
    #                  strides=1,
    #                  kernel_initializer = 'glorot_uniform')(UpSampling1D(size = 2)(conv9))

    up2 = Conv1D(64,
                 2,
                 padding='same',
                 activation='relu',
                 strides=1,
                 kernel_initializer='glorot_uniform')(UpSampling1D(size=2)(drop1))
    concat2 = Concatenate(axis=-1)([conv4, up2])
    conv11 = Conv1D(64,
                    3,
                    padding='same',
                    activation='relu',
                    strides=1,
                    kernel_initializer='glorot_uniform')(concat2)
    conv12 = Conv1D(64,
                    3,
                    padding='same',
                    activation='relu',
                    strides=1,
                    kernel_initializer='glorot_uniform')(conv11)

    up3 = Conv1D(32,
                 2,
                 padding='same',
                 activation='relu',
                 strides=1,
                 kernel_initializer='glorot_uniform')(UpSampling1D(size=2)(conv12))
    concat3 = Concatenate(axis=-1)([conv2, up3])
    conv13 = Conv1D(32,
                    3,
                    padding='same',
                    activation='relu',
                    strides=1,
                    kernel_initializer='glorot_uniform')(concat3)
    conv14 = Conv1D(128,
                    3,
                    padding='same',
                    activation='relu',
                    strides=1,
                    kernel_initializer='glorot_uniform')(conv13)

    # classification Level
    lstm1 = LSTM(256, return_sequences=True, dropout=0.5,
                 recurrent_dropout=0.5)(conv14)
    lstm2 = LSTM(512, return_sequences=True, dropout=0.5,
                 recurrent_dropout=0.5)(lstm1)
    flat1 = Flatten()(lstm2)

    dense1 = Dense(len(activities), activation='softmax')(flat1)

    model = Model(input=inputs, output=dense1, name='UNet_LSTM')
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer, metrics=['accuracy'])
    print(model.summary())
    return model


if __name__ == "__main__":
    activities = list(range(1, 28))
    # model = simple_LSTM()
    # model = bidirectional_LSTM()
    # model = conv_LSTM2()
    model = UNet_LSTM()
