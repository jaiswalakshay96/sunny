# write your function here
def readable_timedelta(days) :
    weeks = days //  7
    day = days % 7
    r = '{} week(s)and {} day(s) '.format(weeks,day)
    return r
# test your function
print(readable_timedelta(1))