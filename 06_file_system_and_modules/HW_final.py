import json
import time

start = time.time()

purchases_dict = {}
with open('purchase_log.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        # if i == 10000:
        #     break
        line = json.loads(line.strip())
        purchases_dict[f"{line['user_id']}"] = f"{line['category']}"
del purchases_dict['user_id']

visits_list = []
with open('visit_log.csv', 'r') as log:
    visits = log.readlines()
    visits = list(map(lambda s: s.strip(), visits))
    count = 0
    for j in visits:
        visits_list.append([j.split(',')[0], j.split(',')[1]])
        # count += 1
        # if count == 10000:
        #     break
# for k, v in purchases_dict.items():
#     for visit in visits_list:
#         if visit[0] == k:
#             visit.append(v)
for visit in visits_list:
    if visit[0] in purchases_dict.keys():
        visit.append(purchases_dict[visit[0]])

file = open('funnel.csv', 'w')
file.write('user_id,source,category')
file.write('\n')
for k in visits_list:
    if len(k) == 3 and k[2] != 'не определена':
        file.write(str(k).replace(' ', '').replace('[', '').replace(']', '').replace("'", ''))
        file.write('\n')
file.close()
end = time.time()
print(round(end - start, 2))
