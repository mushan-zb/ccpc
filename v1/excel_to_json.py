import csv
import json


def main():
    user_info = {}

    with open('CCPC2020.csv', 'r', encoding='utf-8') as file:
        rows = csv.reader(file)
        for row in rows:
            info = {
                'id': row[0],
                'name': row[1],
                'organization': row[2],
                'teamMembers': [{'name': row[3]+"(教练)"}, {'name': row[4]}, {'name': row[5]}, {'name': row[6]}],
                'official': False,
                'marker': False,
            }
            if row[-1] != '正式队伍':
                info['official'] = True

            if row[-2] == '女队':
                info['marker'] = True

            user_info[row[0]] = info

    print(user_info)
    with open('CCPC2020.json', 'w', encoding='utf-8') as file:
        json.dump(user_info, file, ensure_ascii=False)


if __name__ == '__main__':
    main()



