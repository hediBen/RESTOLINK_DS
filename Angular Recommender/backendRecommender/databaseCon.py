
import mysql.connector

class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='21989176', host='127.0.0.1', database='graduationproject', use_pure=False)
        self.cursor = self.connection.cursor()


    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()


    def selectAll(self):
        data = []
        users = []
        items = []
        ratings = []

        self.cursor.execute("SELECT GlobalRatings, userID, placeID from reviews;")
        rows = self.cursor.fetchall()

        for r in rows:
            ratings.append(r[0])
            users.append(r[1])
            items.append(r[2])

        data.append(users)
        data.append(items)
        data.append(ratings)

        return data
    
    
    def getName(self,iid):
        self.cursor.execute("SELECT name from restaurants WHERE placeID = " +str(iid)+ ";")
        rows = self.cursor.fetchall()  
        return rows[0]
    
    
    def CreatetUser(self ,uid):
        self.cursor.execute("INSERT INTO users (idFirebase) VALUES ('" +str(uid)+ "');")
        self.connection.commit()        
        
        return "USER CREATED"

    def getUser(self,uid):
        self.cursor.execute("SELECT userID from users WHERE idFirebase = " +str(uid)+ ";")
        rows = self.cursor.fetchall()
        return rows[0]
    
    def getRestoName(self):
        self.cursor.execute("select distinct name from restaurants r inner join reviews rv on rv.placeID = r.placeID group by r.name having avg(rv.GlobalRatings)>5 ;")
        rows = self.cursor.fetchall()
        return rows


    
    def RateRestaurant(self ,RestaurantId,value,uid):
        self.cursor.execute("INSERT INTO reviews (GlobalRatings,userID,placeID) VALUES ("+str(value)+","+"(select userID from users where idFirebase = \""+str(uid)+"\")" +", (SELECT placeID from restaurants where name= \""+RestaurantId+"\"));")
        self.connection.commit()
        return 'restaurant rated'
    
    def NearRestaurants(self,uid):
        self.cursor.execute("select distinct distance , name from restaurants r inner join allpossibledistances rv on rv.placeID = r.placeID where rv.distance<1 and rv.userID = " +str(uid)+ " ;")
        rows = self.cursor.fetchall()
        return rows


