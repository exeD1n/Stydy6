from itertools import zip_longest

def parsing_csv():
    user_open = open ('users.csv', 'r', encoding="utf-8")
    hobby_open = open ('hobby.csv', 'r', encoding="utf-8")
    
    user_array = []
    for us in user_open:
        user_array.append(us.replace(","," ").rstrip())
    print(user_array)
    
    hobby_array = []
    for hb in hobby_open:
        hobby_array.append(hb.rstrip())
    print(hobby_array) 
    
    iterator = ((a,b) for a,b in zip_longest(user_array, hobby_array))
    info = dict(iterator)
    
    with open ('info.txt', 'r+', encoding='UTF-8') as f:
        f.write(str(info))
    
    
    user_open.close()
    hobby_open.close()
    
            
if __name__ == "__main__":
    parsing_csv()
    