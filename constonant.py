import datetime
def get_datetime():
    dt1 = datetime.datetime.now()
    return dt1.strftime("%d%B,%Y,%A")
monthstr = get_datetime()
urlapi='/data/url'
ERRORNOTIFICATION='/data/errorarn'
SUCCESSNOTIFICATION='/data/successarn'
COMPONENT_NAME='DL_DATA_EXTRACT'
ERROR_MSG=f'NEED ATTENTION *API ERROR /KEY EXPIRED * ON {monthstr}**'
SUCCESS_MSG=f'SUCCESSFULLY EXTRACTED FILES FOR {monthstr}*'
SUCCESS_DRESCRIPTION='SUCCESS'
mugunthan='/data/environment'
