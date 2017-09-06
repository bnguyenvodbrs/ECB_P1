# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:55:33 2017

@author: nguyenb
"""

import sys
import os
sys.path.append(os.path.abspath("X:\\RATINGSADMIN\\DATA_ADMIN\\ECB Coverage Automation\\ECB_CSVFILES\\s3\\legacy-deployment\\aws-feeds\\destinations"))

import oracle
import time


if __name__ == '__main__':
    date_code = time.strftime('%y%m%d')
    filepath = 'X:\\RATINGSADMIN\\DATA_ADMIN\\ECB Coverage Automation\\ECB_CSVFILES\\Uploading'
    filename = os.path.join(filepath ,'ea_csv_%s_rated.csv' %date_code)
    
    hostname = 'amz-p-ora20.dbrs.local'
    login = 'unidb'
    password = 'fnRjn5LLuuZLAJLQLuQr'
    sid = 'BRAPP'
    dir_name = 'ECB_DIR' #'/rsdsdbdata/userdirs/04'
    
    db = oracle.BrappDatabase(hostname, login, password, sid)
    db.upload(filename = filename)

