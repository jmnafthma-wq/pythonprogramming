my_dict={'banana':3,'apple':1,'cherry':2,'date':43}
print("original list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("ascending order:",asorted_dict)
dsorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("decsending order:",dsorted_dict)
