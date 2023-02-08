
from fastapi import FastAPI
import datetime
from peewee import * 
DATABASE = 'tweepee1.db'

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
	class Meta:
		database = database
class User(BaseModel):
	username = CharField(unique=True)
	password = CharField()
	email = CharField()
	join_date= DateTimeField()

class Post(BaseModel):
	username_id = ForeignKeyField(User)
	content = CharField()
	join_date= DateTimeField(default=datetime.datetime.now)

class Likes(BaseModel):
    username = ForeignKeyField(User)
    post_id = ForeignKeyField(Post)

def create_tables():
	with database:
            database.create_tables([User])
            database.create_tables([Post])
            database.create_tables([Likes])
if __name__ == "__main__":
	create_tables()

app1 = FastAPI()


@app1.get("/")
def read_root():
    return {"Hello": "World"}

@app1.get("/users")
def users():
    user_table = []
    for id in User.select():
        user_table.append({'username':id.username,'password':id.password,'email':id.email,'join_date':id.join_date})
    return user_table
@app1.get('/posts')
def post_tab():
    post_table = []
    for id in Post.select():
        post_table.append({'username':id.username_id,'text':id.content,'post_date':id.join_date})
    return post_table

@app1.get("/users/{userid}")
def get_user(userid: str):
    user_table = User.select()
    for id in user_table:
        if id.username == userid:
            return {'username':id.username,'password':id.password,'email':id.email,'join_date':id.join_date}
@app1.get("/like/{user_id}&&{post_id}")
def like(user_id: int,post_id:int):
    Likes.create(user_id=user_id,post_id=post_id)

@app1.get("/unlike/{user_id}/{post_id}")
def unlike(user_id: int,post_id:int):
    q=Likes.delete().where(Likes.user_id==user_id & Likes.post_id==post_id)
    q.execute()

@app1.get("/del_post/{post_id}")
def del_post(post_id:int):
    q=Posts.delete().where(Posts.id==post_id)
    q.execute()


    