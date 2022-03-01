import pickle
import json
import numpy as np
__phones = None
__data_columns = None
__model = None

def get_estimated_price(phone_make,OS,ROM,RAM,screen_size,back_camera,front_camera,Battery,Rating,Likes,specs_score):
    phone_index = __data_columns.index(phone_make.lower())
    try:
        phone_index = __data_columns.index(phone_make.lower())
    except:
        phone_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = OS
    x[1] = ROM
    x[2] = RAM
    x[3] = screen_size
    x[4] = back_camera
    x[5] = front_camera
    x[6] = Battery
    x[7] = Rating
    x[8] = Likes
    x[9] = specs_score
    x[phone_index] = 1
    if phone_index>=0:
        x[phone_index] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __phones
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __phones = __data_columns[10:]
    global __model
    if __model is None:
        with open('./artifacts/kenya_phone_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
def get_phone_names():
    return __phones
def get_data_columns():
    return __data_columns
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_phone_names())
    print(get_estimated_price('Samsung',1,128,6.0,6.40,2527200,20.0,6000,4.3,30,100))
    print(get_estimated_price('Nokia',1,16,2.0,6.0,1036800,8.0,3500,4.5,15,51))
    print(get_estimated_price('Google',1,64,4.0,5.0,2073600,8.0,2700,2.9,11,60))

