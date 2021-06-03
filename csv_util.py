# from connection import db_conn
import pandas as pd

def getResponse(foracid):
    print("foracid: {}".format(foracid))
    
    # df = pd.read_csv('./Recurrent_Trans.csv', usecols=[*range(0,7)], 
    #              names=['period', 'src_account', 'datetime', 'amount', 'dest_account', 'dest_bank', 'tran_particulars']
    #              , header=None, converters={'src_account':str,'dest_account':str})

    df = pd.read_csv('./api_db.csv', usecols=[*range(0,7)], names=['cifId', 'srcAcct', 'destAcct', 'amount', 'beneficiaryName', 'destBankCode', 'destBankName'], header=None, converters={'srcAcct':str,'destAcct':str})
    dd = df[df['srcAcct'] == foracid]
    
    return dd.to_dict('records')


def getCBResponse(cifId):
    print("cifId: {}".format(cifId))


    df = pd.read_csv('./api_db.csv', usecols=[*range(0,7)], names=['cifId', 'srcAcct', 'destAcct', 'amount', 'beneficiaryName', 'destBankCode', 'destBankName'], header=None, converters={'srcAcct':str,'destAcct':str})
    
    return df[df['cifId'] == cifId].to_dict('records')
