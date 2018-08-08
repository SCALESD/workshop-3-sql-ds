#!/usr/bin/python

import csv
from itertools import groupby
import datetime
import pymysql

from config import get_config
from constants import PARKING_METER_TRANSACTION_DATA_FILE, PRICE_PER_HOUR


class Transaction:
    MAX_DURATION = 10  # 8AM - 6PM

    def __init__(self, data):
        self.pole = { 'pole_id': data['pole_id'], 
                      'latitude': data['latitude'],
                      'longitude': data['longitude'] }
        if 'trans_amt' in data:
            self.amount = float(data['trans_amt']) / 100
            self.duration = self.amount / PRICE_PER_HOUR
        if 'trans_start' in data:
            self.start = data['trans_start']
        if 'meter_expire' in data:
            self.expire = data['meter_expire']
		
    @classmethod
    def transactions(cls, date, bounding_box):
        config = get_config()

        conn = pymysql.connect(host=config['ParkingDataHost'],
							   user=config['ParkingDataUsername'],
							   passwd=config['ParkingDataPassword'],
							   db=config['ParkingDataDB'],
							   cursorclass=pymysql.cursors.DictCursor)

        lat_a, lng_a, lat_b, lng_b = bounding_box
		
        query = "SELECT `pole_id`,`trans_amt`,`trans_start`,`meter_expire`,`latitude`,`longitude` FROM `parking-meter-transaction` INNER JOIN `parking-meter-location` ON `pole`=`pole_id` WHERE DATE(`trans_start`)='{0}' AND `latitude` BETWEEN {1} AND {2} AND `longitude` BETWEEN {3} AND {4}".format(date, lat_a, lat_b, lng_a, lng_b)

        transactions = []
        with conn.cursor() as cursor:
            cursor.execute(query)
            transactions = list(map(lambda row: Transaction(row), cursor.fetchall()))

        return transactions            
    

    @classmethod
    def transaction_poles(cls, date, bounding_box):
        conn = pymysql.connect(host=host,
							   user=user,
							   passwd=password,
							   db=database,
							   cursorclass=pymysql.cursors.DictCursor)

        lat_a, lng_a, lat_b, lng_b = bounding_box
		
        query = "SELECT `pole_id`,`latitude`,`longitude` FROM `parking-meter-transaction` INNER JOIN `parking-meter-location` ON `pole`=`pole_id` WHERE DATE(`trans_start`)='{0}' AND `latitude` BETWEEN {1} AND {2} AND `longitude` BETWEEN {3} AND {4} GROUP BY `pole_id`".format(date, lat_a, lat_b, lng_a, lng_b)

#        print(query)
        
        transactions = []
        with conn.cursor() as cursor:
            cursor.execute(query)
            transactions = list(map(lambda row: Transaction(row), cursor.fetchall()))

        return transactions            
    
    
    
    @classmethod
    def transactions_for_day(cls, num_day_of_2017):
        if not hasattr(cls, '_transactions_day_map'):
            transactions = cls.transactions()
            by_day = groupby(transactions, lambda t: t.start[:10])  # First 10 digits are %Y-%m-%d
            cls._transactions_day_map = {date: list(grouped_transactions) for date, grouped_transactions in by_day}

        date = (datetime.datetime(2017, 1, 1) + datetime.timedelta(num_day_of_2017 - 1)).strftime('%Y-%m-%d')

        return cls._transactions_day_map[date] if date in cls._transactions_day_map else []
