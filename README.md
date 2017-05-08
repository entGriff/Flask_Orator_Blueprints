# Flask ORM Blueprints
### Flask Blueprints app with Orator ORM for Laravel's Eloquent lovers and not only for them.  

---
 If You are Programmer who can't code without Active record pattern, who has experience with Laravel Eloquent or just  like beautiful ORM - this repository if for you.   
 
 The Idea of this repository comes from  [Twittor api], which inspired me to do implementation of Orator(AN ACTIVERECORD ORM FOR PYTHON) and Flask Blueprints architecture.
 [tittor api]
 ---
 
 
### Requirements
```sh
$ pip install -r requirements.txt
```
If you have problem with installing Orator using pip, you can try:
```sh
$ easy_install orator
```

### Migrations and seeds
> Repository already contains migration and seed files, but using Orator you can generate they yourself.

1. Setup the needed tables:
    `python db.py migrate`

2. Insert data into newly created tables.
    `python db.py db:seed`

### Seeded data :

![migrated_tables](https://cloud.githubusercontent.com/assets/2203893/25797167/2b467f82-33ed-11e7-8409-d98e9d5ddece.gif)

### Run application
```sh
$ python manage.py runserver
```

### Usage :
---
| Operations | URL | Description| Type |
| ------ | --------- |----------|-------|
| GET | http://127.0.0.1:5000/users | Returns all users from users table | READ|
| POST | http://127.0.0.1:5000/users | Creates new user | CREATE|
| GET | http://127.0.0.1:5000/users/{user_id} | Returns user by user id | READ|
| PATCH | http://127.0.0.1:5000/users/{user_id} | Updates user by user id | UPDATE|
| GET | http://127.0.0.1:5000/users/{user_id}/messsages | Returns messages by user id | READ|
| POST | http://127.0.0.1:5000/users/{user_id}/messsages | Creates meesage by user id | CREATE|
| GET | http://127.0.0.1:5000/users/{user_id}/following | Returns user following by user id | READ|
| GET | http://127.0.0.1:5000/users/{user_id}/followers | Returns user followers by user id | READ|
| PUT | http://127.0.0.1:5000/users/{user_id}/following/{followed_user_id} | Follow user | CREATE|
| DELETE | http://127.0.0.1:5000/users/{user_id}/following/{followed_user_id} | Unfollow user | DELETE|
| GET | http://127.0.0.1:5000/messages/{message_id} | Returns messages by message id | READ|
| PATCH | http://127.0.0.1:5000/messages/{message_id} | Updates message by message id | UPDATE|
| DELETE | http://127.0.0.1:5000/messages/{message_id}  | Removes message by message id | DELETE|


 [Twittor api]:  <https://github.com/sdispater/twittor-api>
