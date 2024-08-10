import json


if __name__=='__main__':
    # file = open("./kg_crime.json","r")
    # data=[]
    # accusation=set()
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     accusation.add(line['crime_big'])
    #     accusation.add(line['crime_small'])
    # # print(len(accusation))
    # for item in accusation:
    #     print(item)
    # file = open("./final_all_data/final_test.json",'r',encoding='utf-8')
    # data = []
    # accusation = set()
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     data.append(line)
    # file = open("./final_all_data/restData/rest_data.json",'r',encoding='utf-8')
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     data.append(line)
    # file = open("./final_all_data/first_stage/test.json",'r',encoding='utf-8')
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     data.append(line)
    # file = open("./final_all_data/first_stage/train.json",'r',encoding='utf-8')
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     data.append(line)
    # file = open("./final_all_data/exercise_contest/data_train.json",'r',encoding='utf-8')
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     data.append(line)
    # file = open("./final_all_data/exercise_contest/data_test.json",'r',encoding='utf-8')
    # for lines in file.readlines():
    #     line = json.loads(lines)
    #     data.append(line)
    # file = open("./final_all_data/exercise_contest/data_valid.json",'r',encoding='utf-8')
    # for lines in file.readlines():
    #     line = json.loads(lines)
    # data.append(line)


    # for i in range(len(data)):
    #     for item in data[i]['meta']['accusation']:
    #         accusation.add(item)
    # print(len(accusation))
    # for item in accusation:
    #     print(item)
    file1 = "./law.txt"
    file2 = "./law1.txt"
    file_1=open(file1,'r')
    file_2=open(file2,'r')
    accusation=set()
    for lines in file_1.readlines():
        accusation.add(lines)
    for lines in file_2.readlines():
        accusation.add(lines)
    # print(len(accusation))
    for item in accusation:
        print(item[:-1])
        # break
