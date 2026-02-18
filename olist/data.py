from pathlib import Path
import pandas as pd


class Olist:
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
       def get_data(self):
        # 1. Verilerin olduğu gizli global klasörü buluyoruz
        csv_path = Path.home().joinpath(".workintech/olist/data/csv")

        data = {}
        # 2. Klasördeki tüm dosyaları tek tek dönüyoruz
        for file in csv_path.iterdir():
            if file.suffix == '.csv':
                # İsim temizleme: 'olist_orders_dataset.csv' -> 'orders'
                key = file.name.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
                data[key] = pd.read_csv(file)

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
