import pandas as pd
from pathlib import Path


dataStore = {}
text_file_path3 = r"C:\Users\THUNDEROBOT\Documents\Unreal Projects\trick\Content\Developers\botwins4.txt"
text_file_path2 = r"C:\Users\THUNDEROBOT\Documents\Unreal Projects\trick\Content\Developers\botwins3.txt"
text_file_path = r"C:\Users\THUNDEROBOT\Documents\Unreal Projects\trick\Content\Developers\botwins2.txt"
csv_file_path = 'output.csv'
# lst1 = [1,2,3,4,5]
# lst2 = [3,5,8,9,1]
# lst3 = [3,-11,0,2,7]
lst = [[], [], [], [], [], [], [], [], [], []]
with open(text_file_path2, 'r') as text_file:
    # Прочитать содержимое текстового файла
    single_line_info2 = text_file.read()
    text_file.close()
with open(text_file_path3, 'r') as text_file:
    # Прочитать содержимое текстового файла
    single_line_info3 = text_file.read()
    text_file.close()
with open(text_file_path, 'r') as text_file:
    # Прочитать содержимое текстового файла
    single_line_info = text_file.read()
    single_line_info = single_line_info + single_line_info2 + single_line_info3
    single_line_info = single_line_info.split()
    single_line_info_sorted = single_line_info.copy()
    #Заменяем повторяющиеся строки 0,0,0.... и добавляем количество побед
    for i in range(0, len(single_line_info), 10):
        for n in range(10, len(single_line_info), 10):
            if i + n >= len(single_line_info):
                pass
            else:
                if single_line_info[i] == single_line_info[i + n]:
                    single_line_info_sorted[i + 19] = int(single_line_info_sorted[i + 19]) + int(single_line_info_sorted[i + 9])
                    for s in range(10):
                        single_line_info_sorted[i + s] = '0'
    single_line_info_no_garbage = single_line_info_sorted.copy()
    # print(single_line_info_sorted)
    i = 0
    while i < len(single_line_info_sorted):
        if single_line_info_sorted[i] == '0':
            single_line_info_sorted.pop(i) * 10
        else:
            i += 10
    for i in range(0, len(single_line_info_sorted), 10):
        for n in range(10):
            lst[i % 10 + n].append(int(single_line_info_sorted[i + n]))
    text_file.close()
numbers = []
for i in range(0, len(single_line_info_sorted), 10):
    numbers.append(i // 10 + 1)

data = dict(BotNumber=numbers, Speed=lst[0], TurnRate=lst[1], SurviveTime=lst[2], PunchsDone=lst[3], DeadByTimer=lst[4],
            BasicPunchLvl=lst[5],
            SpawnLocationX=lst[6], SpawnLocationY=lst[7], Mass=lst[8], WinsAchieved=lst[9])

df = pd.DataFrame(data)
# print(df)
sorted_df = df.sort_values(by='Mass')
sorted_df.to_csv('output.csv', sep=';', index=False)

# print(Path('output.csv').read_text())
