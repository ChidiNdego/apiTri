# from connection import db_conn

# def getResponse(foracid):
#     print("foracid: {}".format(foracid))
#     resSet = {}
#     resSetList = []
#     cursor = db_conn.cursor()
#     query = "select foracid,tran_amt,ben_acct_no, dest_bank_name from [RSVREDONG].[dbo].[rec_jan_to_apr_htd] where FORACID='{}'".format(foracid)
#     cursor.execute(query)

#     dd = cursor.fetchall()

#     for row in dd: 
#         resSet['foracid'] = row[0]
#         resSet['tran_amt'] = str(row[1])
#         resSet['ben_acct_no'] = row[2]
#         resSet['dest_bank_name'] = row[3]
#         resSetList.append(resSet)
        

#     cursor.close()

#     return resSetList
