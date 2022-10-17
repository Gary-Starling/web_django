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

http://127.0.0.1:8000/v1/users/                		#Показать все(get)

http://127.0.0.1:8000/v1/users/<int:pk>/           	#Показать конкретный по id(get)

http://127.0.0.1:8000/v1/users/sortedByAge/ 		#Показать отсортированный по возрасту(get)

http://127.0.0.1:8000/v1/users/sortedById/   		#Показать отсортированный по id(get)

http://127.0.0.1:8000/v1/post/AddNew/                   #Добавить нового юзера(post/create)

http://127.0.0.1:8000/v1/put/ChangeUser/<int:pk>/    	#Изменить данные юзера(put)
    
http://127.0.0.1:8000/v1/delete/<int:pk>/               #Удалить юзера по id(delete)
	
--jwt--
http://127.0.0.1:8000/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     #получить jwt

http://127.0.0.1:8000/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    #обновить токен

http://127.0.0.1:8000/v1/jwt/GetPUT/<int:pk>/', ApiUserJwtInfoView.as_view()),                  #получитиь данные юзера по id(jwt)




 





####CRUD
//create
'''
POSTMAN

query

    POST: http://127.0.0.1:8000/v1/post/AddNew/ 
    
    body : 
	    {
	    "name": "Myname",
	    "age": 17,
	    "date_reg": "2022-08-05T8:30:10Z"
	    }
	    
   response:
	    {
	    "AddUser": {
			"id": 31,
			"name": "Myname",
			"age": 17,
			"date_reg": "2022-08-05T08:30:10Z"
	    		}
	    }

'''


//read
'''
POSTMAN

query

    GET: http://127.0.0.1:8000/v1/users/
    
    body:no
    
	response:
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


//update
'''

query

    PUT: http://127.0.0.1:8000/v1/put/ChangeUser/<id>/ 
    
    body : 
	    {
	    "name": "new",                      //change name
	    "age": 17,                          //change age
	    "date_reg": "2022-08-05T8:30:10Z"   //change date
	    }

response:
	  {
	    "Put": 
	    {
		"id": 32,
		"name": "HideMePls",
		"age": 30,
		"date_reg": "2022-11-07T08:30:10Z"
	    }
	  }

'''

//delete

'''

query

    DELETE: http://127.0.0.1:8000/v1/delete/<id>/
    body : no
    
response:
	{
	    "Delet": "delete user with id = 2"
	}

'''
