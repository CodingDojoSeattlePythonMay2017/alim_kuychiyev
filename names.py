student = [
     {'first_name':'Michael', 'last_name' : 'Jordan'},
     {'first_name':'John', 'last_name' : 'Rosales'},
     {'first_name':'Mark', 'last_name' : 'Guillen'},
     {'first_name':'KB', 'last_name' : 'Tonel'}
]

for item in student:
    print item['first_name'],item['last_name']



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names(dictin):
    count = 1
    for key in dictin:
        print key
        for i in dictin[key]:
            print count, "- " + i['last_name'], i['first_name'],len(i['last_name']) + len(i['first_name'])
            count +=1

names(users)
