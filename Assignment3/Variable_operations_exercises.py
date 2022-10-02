##variable operation exercises
sub_code="sub"
subnr_int=2
subnr_str="2"
#print(sub_code+subnr_int) ##TypeError:can only concatenate str (not "int") to str
print(sub_code+subnr_str)

print(sub_code+" "+subnr_str)
print(sub_code+" "+(subnr_str*3))
print((sub_code+subnr_str)*3)
print((sub_code*3)+""+(subnr_str*3))
