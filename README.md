# web_django

##pages
http://127.0.0.1:8000/

http://127.0.0.1:8000/about

http://127.0.0.1:8000/contacts

http://127.0.0.1:8000/details

http://127.0.0.1:8000/database     (on this page you can delete users from database)

http://127.0.0.1:8000/database/add (use to add new user to database)

http://127.0.0.1:8000/database/<id> (show detail user)


###API

127.0.0.1:8000/api/v1/users/                     #Показать все(get)

127.0.0.1:8000/api/v1/users/<int:pk>/'           #Показать конкретный по id(get)

127.0.0.1:8000/api/v1/users/sortedByAge          #Показать отсортированный по возрасту(get)

127.0.0.1:8000/api/v1/users/sortedById           #Показать отсортированный по id(get)

127.0.0.1:8000/api/v1/get/all/                   #Показать все, но через APIView

127.0.0.1:8000/api/v1/post/AddNew/               #Добавить нового юзера(post/create)

127.0.0.1:8000/api/v1/post/update/<int:pk>/	 #Удалить юзера по id

127.0.0.1:8000/api/v1/post/Delete/<int:pk>/      #Удалить юзера по id(delete)


####CRUD
//create
'''
POSTMAN

query

    POST:127.0.0.1:8000/api/v1/post/AddNew/
    
    body : 
    {
    "name": "Myname",
    "age": 17,
    "date_reg": "2022-08-05T8:30:10Z"
    }

response

    {
    "AddUser": {
        	"id": 31,
        	"name": "Myname",
        	"age": 17,
        	"date_reg": "2022-08-05T08:30:10Z"
    		}
    }

json
'''


//read
'''
POSTMAN

query

    GET:127.0.0.1:8000/api/v1/get/all
    
    body:no
    
response

json
{
    "Users": [
        {
            "id": 1,
            "name": "Igor",
            "age": 29,
            "date_reg": "2022-11-07T08:29:10Z"
        },
        {
            "id": 2,
            "name": "Gary",
            "age": 25,
            "date_reg": "2022-10-09T11:30:00Z"
        }
        ]
'''
#read+


//update
'''

query

    PUT:127.0.0.1:8000/api/v1/post/update/<id-user>/
    body : {
    "name": "new",                      //change name
    "age": 17,                          //change age
    "date_reg": "2022-08-05T8:30:10Z"   //change date
    }

response

json

    {
    "Put": {
        "id": 32,
        "name": "HideMePls",
        "age": 30,
        "date_reg": "2022-11-07T08:30:10Z"
    }
    }
}

'''

//delete

'''

query

    DELETE:127.0.0.1:8000/api/v1/post/Delete/<id>/
    body : no
    
response

json
{
    "Delet": "delete user with id = 2"
}

'''
