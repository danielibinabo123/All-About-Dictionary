demo={"name":"DANIEL","age":5,"country":"Nigeria","is_flying":False} 
print(f"name:{demo['name']}")
print(f"name:{demo.get('name')}")    

demo['gender']="male"
demo['DOB']="2021-01-01"
print(demo)

demo["age"]=14
print(demo)
print("\n==============\n")
for key in demo:
    print(f"{key}:{demo[key]}")
