#
import json

data1 = {

        'Name': 'Jade Fletcher',
        'Age': 24,
        'city': 'New York, NY',
        'interests': ['Gaming', 'Baseball', 'Cooking'],
        'is_student': False
}

with open('data1.json','w') as json_file:
    
    json.dump(data1,json_file,indent=4)
    
print("Data has been written to data1.json")



#
with open('data1.json','r') as json_file:
    
    loaded_data = json.load(json_file)   

print("Sucessfully able to read data1.json")
print(loaded_data)



loaded_data['age'] = 24 #<-ints
loaded_data['interests'].append('Secret Hobby')


loaded_data['interests'].remove('Secret Hobby')


with open('data1.json','w') as json_file:
    
    json.dump(loaded_data,json_file,indent=4)
    
print("Data has been re-written to data1.json")
