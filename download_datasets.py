# downloads the zstd compressed datasets from the google drive

import os
import requests
import shutil
import sys
import zipfile

part_ids = [ 
    '1PFoKOPJA_WSt4b3w_6PkGt2GRM02QYgc',
    '11nQacibpIphoxuyoRW4NU0AD-a4Eb4xM',
    '18e5uROegtMLySFpbAm1l9ZazDahrWR2-',
    '1CZpiY_rKWeHKapWnrZOlNKp58WsLfke2',
    '1W9GYYbqQOkImBaAju3dbQnhEq01YVMc3',
    '1XbrQJBKBH04bFNXw2kcj_L-ePv9uAXEH',
    '1F4w2h5t65egvNL-z38cXs27G_-CQ4J1c',
    '1Q2RD6i7QnbSHMu2WkuEJfCqjmOELCwIn',
    '1IS4hguKyWINqfuEoRh_JxVWiSD5rrzOj'
]

def download_file_from_google_drive(id, destination):
    URL = f"https://drive.usercontent.google.com/download?export=download"
    
    session = requests.Session()
    response = session.get(URL, stream=True)
    token = None
    params = {'id': id, 'export': 'download'}
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
    if token:
        params['confirm'] = token
        response = session.get(URL, params=params, stream=True)