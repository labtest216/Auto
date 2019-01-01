

# Install mongodb server.
# Install python mongodb packages.
# Start mongodb server.

import pymongo


class db:

    connection_string = "mongodb://localhost:27017/"
    myclient = pymongo.MongoClient(connection_string)
    mydb = myclient["mydatabase"]
    samples_table = mydb["samples", "hw_config"]


]
#x = samples_table.insert_many(report)
for x in samples_table.find():
    print(x)
