# from connection import db_conn
import pandas as pd

def getResponse(foracid):
    print("foracid: {}".format(foracid))
    
    # df = pd.read_csv('./Recurrent_Trans.csv', usecols=[*range(0,7)], 
    #              names=['period', 'src_account', 'datetime', 'amount', 'dest_account', 'dest_bank', 'tran_particulars']
    #              , header=None, converters={'src_account':str,'dest_account':str})

    df = pd.read_csv('./api_db.csv', usecols=[1,2,3,4,5,6],
                 names=['srcAcct', 'destAcct', 'amount', 'beneficiaryName','destBankCode','destBank'],
                 skiprows=1,
    converters={'srcAcct': str, 'destAcct':str,'destBankCode':str})
    
    return df[df['srcAcct'] == foracid][['srcAcct', 'destAcct', 'beneficiaryName', 'destBank', 'destBankCode', 'amount']].to_dict('records')


def getCBResponse(cifId):
    print("cifId: {}".format(cifId))

    df = pd.read_csv('./api_db.csv', usecols=[0,1,7,8,3],
                 names=['cif_id', 'foracid', 'txnDateTime', 'txnParticulars', 'amount'],
                 skiprows=1,
    converters={'cif_id': str, 'foracid':str,'txnDateTime':str})
    
    return df[df['cif_id'] == cifId][['foracid', 'txnDateTime', 'txnParticulars', 'amount']].to_dict('records')
