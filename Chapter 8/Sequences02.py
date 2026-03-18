import copy

various = ["John", 42, True, [1, 2, 3]]
var2 = various			# var2 refers to the same object!
var2[2]=3
var3 = various[:]
var3[2] = "OK"
var3[3][2] = "o, no"
var4= copy.deepcopy(various)
var4[3][2]="OK"

print(various, var2, var3, var4)