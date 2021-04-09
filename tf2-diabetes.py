from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import pandas as pd
import mlflow



data_d = load_diabetes()
pd.DataFrame(data_d.data).to_csv("diabetes_data.csv")
data = data_d.data
target = data_d.target


target = target-target.mean(axis=0)/target.std()
train_data , test_data , train_target, test_target = train_test_split(data,target,
                                                                      test_size=0.1)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dropout
from tensorflow.keras import regularizers



earlystopping = EarlyStopping(monitor='val_loss')
#earlystoping = EarlyStopping(monitor='val_accuracy',patience=5,min_delta=0,01,mode='max')

def get_model():
     model = Sequential([
            Dense(128,activation='relu', input_shape =(train_data.shape[1],)),
            Dense(128,activation='relu'),
            Dense(128,activation='relu'),
            Dense(128,activation='relu'),
            Dense(128,activation='relu'),
            Dense(128,activation='relu'),
            Dense(1)
        ])
     return model



def get_regularized_model(wd,rate):
    model = Sequential([
        Dense(128, kernel_regularizer=regularizers.l2(wd),
                    activation='relu',
                    input_shape=(train_data.shape[1],)),
        Dropout(rate),
        Dense(128, kernel_regularizer=regularizers.l2(wd),activation='relu'),
        Dropout(rate),
        Dense(128, kernel_regularizer=regularizers.l2(wd),activation='relu'),
        Dropout(rate),
        Dense(128, kernel_regularizer=regularizers.l2(wd),activation='relu'),
        Dropout(rate),
        Dense(128, kernel_regularizer=regularizers.l2(wd),activation='relu'),
        Dropout(rate),
        Dense(128, kernel_regularizer=regularizers.l2(wd), activation='relu'),
        Dropout(rate),
        Dense(128, kernel_regularizer=regularizers.l2(wd), activation='relu'),
        Dropout(rate),
        Dense(1)
    ])
    return model
#model = get_model()
model = get_regularized_model(1e-5,0.3)

model.compile(optimizer='adam',loss='mse',metrics=['mae'])
with mlflow.start_run():
    # Automatically capture the model's parameters, metrics, artifacts,
    # and source code with the `autolog()` function
    mlflow.set_experiment('haris-diabetes-12-03-2021')
    mlflow.set_tags({'name ': 'tensorflow2 diabetes'})
    mlflow.tensorflow.autolog()
    model.fit(train_data, train_target, validation_split=0.15,
            batch_size=64, epochs=100,verbose=False,
            callbacks=[earlystopping])
    model.evaluate(test_data, test_target, verbose=2)
    model.save('model_folder/')
    mlflow.tensorflow.log_model(tf_saved_model_dir='model_folder/',
                               tf_meta_graph_tags=['serve'],
                               tf_signature_def_key='serving_default',
                               artifact_path='tensor')
    mlflow.log_artifact('diabetes_data.csv')
    mlflow.end_run()
    #run_id = mlflow.active_run().info.run_id
    #artifact_path='model'
    #model_uri = "runs:/{run_id}/{artifact_path}".format(run_id=run_id, artifact_path=artifact_path)
    #model_details = mlflow.register_model(model_uri=model_uri , name='tensorflow diabetes example')
    # log model


    #receiver_fn = tf.estimator.export.build_raw_serving_input_receiver_fn(feat_specifications)
    #temp = tempfile.mkdtemp()
    #model.export_saved_model('/Users/charalampossouris/ml_python',model)

print('Harry is happy with this training ')




