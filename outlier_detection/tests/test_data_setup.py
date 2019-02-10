# -*- coding: utf-8 -*-
import pandas as pd
import os
from influxdb import DataFrameClient
import influxdb


def export_influx_data(dbname, query, host='raspberrypi', port=8086):
    """Instantiate the connection to the InfluxDB client."""

    user = 'root'
    password = 'root'
    client = DataFrameClient(host, port, user, password, dbname)
    dataframe = client.query(query)
    dataframe = dataframe[next(iter(dataframe))]
    
    dataframe.to_csv(os.path.dirname(os.path.abspath(__file__)) + '/influx_data.csv', index_label='time')
    return dataframe

def import_dataframe():
    df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/influx_data.csv', index_col=[0])
    df.index = pd.to_datetime(df.index)
    df.index = df.index.tz_localize('UTC')
    # df.index.name = None
    return df

#export_influx_data(dbname='environment',   query="SELECT value FROM weather WHERE (variable =~ /^Temperature$/ AND unit=~ /^Celsius$/ AND region =~ /^living_room$/) AND time >= now() - 6h limit 10")

#import_dataframe()