#!/usr/bin/python

var1 = 'testing python script in docker container triggered by jenkins'
print(var1)

var2 = 9
var3 = 5

print("{} + {} = {}".format(var2, var3, (var2+var3)))

exit(0)
