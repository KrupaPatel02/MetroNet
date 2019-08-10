import re
from datetime import datetime

regex = "20\d{2}(-|\/)((0[1-9])|(1[0-2]))(-|\/)((0[1-9])|([1-2][0-9])|(3[0-1]))(T|\s)(([0-1][0-9])|(2[0-3])):([0-5][0-9]):([0-5][0-9])"
regex1 = "([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"

def validateTimeStamp(timestamp):
    print("Started validating")
    if re.search(regex, timestamp) or re.search(regex1, timestamp):
        print("Valid")
    else:
        print("Not valid")


datetime1 = "2017-02-14 19:30:52"
validateTimeStamp(datetime1)

datetime2 = "2017-02-14"
validateTimeStamp(datetime2)

# current date and time
# now = datetime.now()
# timestamp = datetime.timestamp(now)
#
# date_obj = datetime.fromtimestamp(timestamp)
# validateTimeStamp(date_obj)

# validateTimeStamp(timestamp)
