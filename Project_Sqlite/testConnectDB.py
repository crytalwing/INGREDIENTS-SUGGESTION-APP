#%%
import sqlite3

mydb =sqlite3.connect("APP.db")
cursor = mydb.cursor()
cursor.execute('''Create Table Foods
            (
	        Food char(100) Primary key,
	        TypeFood char(50),
	        SarvingSize int,
	        TypeSarving char(10),
	        Cal int
            )''')

cursor.execute('''create table Users
            (
	            IdUser INTEGER PRIMARY KEY AUTOINCREMENT,
	            Phone char(10) not null,
	            Passwords char(10) not null,
	            NameUser char(50) not null,
	            Height int not null,
	            Weights float not null,
	            Age int not null,
	            Gender char(10) not null,
	            Active int default 0,
	            Currents int default 0
            )''')

cursor.execute('''create table Weekly
            (
	            Id integer  PRIMARY KEY AUTOINCREMENT,
	            IdUser int not null,
	            Bmr int not null,
	            TimeUpdate Datetime,
	            constraint [FK_Users_Weekly] Foreign key ([IdUser]) references Users([IdUser])
            )''')
# %%

#%%
cursor.execute("Insert into Foods Values('Apple','Fruits',4,'oz',59)")
cursor.execute("Insert into Foods Values('Banana','Fruits',6,'oz',151)")
cursor.execute("Insert into Foods Values('Grapes','Fruits',1,'cup',100)")
cursor.execute("Insert into Foods Values('Orange','Fruits',4,'oz',53)")
cursor.execute("Insert into Foods Values('Pear','Fruits',5,'oz',82)")
cursor.execute("Insert into Foods Values('Peach','Fruits',6,'oz',67)")
cursor.execute("Insert into Foods Values('Pineapple','Fruits',1,'cup',82)")
cursor.execute("Insert into Foods Values('Strawberry','Fruits',1,'cup',53)")
cursor.execute("Insert into Foods Values('Watermelon','Fruits',1,'cup',50)")
cursor.execute("Insert into Foods Values('Asparagus','Vegetable',1,'cup',27)")
cursor.execute("Insert into Foods Values('Broccoli','Vegetable',1,'cup',45)")
cursor.execute("Insert into Foods Values('Carrots','Vegetable',1,'cup',50)")
cursor.execute("Insert into Foods Values('Cucumber','Vegetable',4,'oz',17)")
cursor.execute("Insert into Foods Values('Eggplant','Vegetable',1,'cup',35)")
cursor.execute("Insert into Foods Values('Lettuce','Vegetable',1,'cup',5)")
cursor.execute("Insert into Foods Values('Tomato','Vegetable',1,'cup',22)")
cursor.execute("Insert into Foods Values('Beef regular cooked','Protein',2,'oz',142)")
cursor.execute("Insert into Foods Values('Chicken cooked','Protein',2,'oz',136)")
cursor.execute("Insert into Foods Values('Tofu','Protein',4,'oz',86)")
cursor.execute("Insert into Foods Values('Egg','Protein',1,'large',78)")
cursor.execute("Insert into Foods Values('Fish Catfish cooked','Protein',2,'oz',136)")
cursor.execute("Insert into Foods Values('Pork cooked','Protein',2,'oz',137)")
cursor.execute("Insert into Foods Values('Shrimp cooked','Protein',2,'oz',56)")
cursor.execute("Insert into Foods Values('Coca-cola','Beverages',1,'can',150)")
cursor.execute("Insert into Foods Values('Milk (1%)','Beverages',1,'cup',102)")
cursor.execute("Insert into Foods Values('Milk (2%)','Beverages',1,'cup',122)")
cursor.execute("Insert into Foods Values('Milk whole','Beverages',1,'cup',146)")
cursor.execute("Insert into Foods Values('OrangeJuice','Beverages',1,'cup',111)")
cursor.execute("Insert into Foods Values('Applecider','Beverages',1,'cup',117)")
cursor.execute("Insert into Foods Values('Yogurt (low-fat)','Beverages',1,'cup',154)")
cursor.execute("Insert into Foods Values('Yogurt (non-fat)','Beverages',1,'cup',110)")
cursor.execute("Insert into Foods Values('Bread,white','CommonMeals',1,'slice',75)")
cursor.execute("Insert into Foods Values('Caesar salad','CommonMeals',3,'cups',481)")
cursor.execute("Insert into Foods Values('Cheeseburger','CommonMeals',1,'sandwich',285)")
cursor.execute("Insert into Foods Values('Hamburger','CommonMeals',1,'sandwich',250)")
cursor.execute("Insert into Foods Values('Dark Chocolate','CommonMeals',1,'oz',155)")
cursor.execute("Insert into Foods Values('Corn','CommonMeals',1,'cup',132)")
cursor.execute("Insert into Foods Values('Pizza','CommonMeals',1,'slice',285)")
cursor.execute("Insert into Foods Values('Potato (low-fat)','CommonMeals',6,'oz',130)")
cursor.execute("Insert into Foods Values('Rice (non-fat)','CommonMeals',1,'cup',206)")
cursor.execute("Insert into Foods Values('Sandwich','CommonMeals',1,'loaf',200)")
mydb.commit()
mydb.close()