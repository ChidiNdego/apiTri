# import pyodbc
# server = '10.234.18.152'
# # database = 'RSVRRealtimeFinacleNG'
# database = 'RSVREDONG'
# username = 'EDOUSER'
# password = 'Stanbic_123#'

# db_conn = pyodbc.connect('Driver={SQL Server};Server='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';')

# print(db_conn.getinfo(0))

# cursor = db_conn.cursor()
# foracid = '9200076526'
# cursor.execute("select foracid,tran_amt,ben_acct_no, dest_bank_name from [RSVREDONG].[dbo].[rec_jan_to_apr_htd] where FORACID='{}'".format(foracid))

# record_count = cursor.fetchone()[0]
# cursor.close()
# print(record_count)