import csv

def parsing_csv():
    user_open = open ('users.csv', 'r', encoding="utf-8")
    hobby_open = open ('hobby.csv', 'r', encoding="utf-8")
    
    user_array = []
    for us in user_open:
        print(us.split(","))
    
    hobby_array = []
    for hb in hobby_open:
        print([hb])
    
    user_open.close()
    hobby_open.close()
    
    
    
    
    # with open ('users.csv', 'r', encoding="utf-8") as f:
    #     reader = csv.reader(f)
    #     print(reader)
    #     for user in reader:
    #         print(user)
                    
    # with open ('hobby.csv', 'r', encoding="utf-8") as f:
    #     reader = csv.reader(f)
    #     for line in reader:
    #         print(line)
            
if __name__ == "__main__":
    parsing_csv()
    