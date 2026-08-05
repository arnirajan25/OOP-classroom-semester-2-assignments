import datetime
print("Date and Time Examples:")
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now())
future=datetime.datetime.today() + datetime.timedelta(days=7)
print("Date after 7 days:",future)
print()
