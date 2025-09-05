import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    """
    Predicts the house price given location, sqft, bhk, bath
    """
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    """
    Returns list of location names
    """
    return __locations


def load_saved_artifacts():
    """
    Loads model and columns from artifacts folder
    """
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    base = os.path.dirname(__file__)   # folder where util.py is located
    columns_path = os.path.join(base, "artifacts/columns.json")
    model_path = os.path.join(base, "artifacts/bangalore_home_prices_model.pickle")

    try:
        with open(columns_path, "r") as f:
            __data_columns = json.load(f)["data_columns"]
            __locations = __data_columns[3:]  # first 3 = sqft, bath, bhk
            print("Loaded locations:", __locations[:5], "...")  # show first few
    except Exception as e:
        print("Error loading columns.json:", e)

    try:
        with open(model_path, "rb") as f:
            __model = pickle.load(f)
            print("Model loaded successfully")
    except Exception as e:
        print("Error loading model:", e)

    print("Loading saved artifacts...done")


# For testing this file standalone
if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("Indira Nagar", 1200, 2, 2))

