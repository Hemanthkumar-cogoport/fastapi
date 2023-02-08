print("Hesfmsf")
import datetime
from peewee import * 
DATABASE = 'tweepee1.db'

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
	class Meta:
		database = database
class User(BaseModel):
	username = CharField(unique=True,primary_key=True)
	password = CharField()
	email = CharField()
	join_date= DateTimeField()

class Post(BaseModel):
	username = ForeignKeyField(User,to_field="username",related_name="User")
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

# User.create(username='luffy',password='meatumeatu',email='hahe@gmail',join_date='23-91-3113')
# User.create(username='zoro',password='saje',email='santoryu@gmail',join_date='23-9-2003')
# User.create(username='naami',password='money',email='lala@gmail',join_date='23-90-3123')
# User.create(username='sanji',password='naamscha',email='naamihe@gmail',join_date='2334-91-113')
# User.create(username='ussop',password='msf',email='ha@gmail',join_date='23-91-2213')
# User.create(username='robin',password='mdsfff',email='sadfsha@gmail',join_date='2-1-2003')
# Post.create(username_id='ussop',content='jssawetwettwgsdvafgavsaf')
# Post.create(username_id='robin',content='jsafhjsaf')
Likes.create(username='luffy',post_id='2')
Likes.create(username='robin',post_id='2')

