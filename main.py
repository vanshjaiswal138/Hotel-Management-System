# Python program to solve
# the given question

# Create class for hotel data.
class Hotel :
	sortParam='name'
	def __init__(self) -> None:
		self.name=''
		self.roomAvl=0
		self.location=''
		self.rating=int
		self.pricePr=0
	
	def __lt__(self,other):
		getattr(self,Hotel.sortParam)<getattr(other,Hotel.sortParam)
	
	# Function to change sort parameter to
	# name
	@classmethod
	def sortByName(cls):
		cls.sortParam='name'

	# Function to change sort parameter to
	# rating.
	@classmethod
	def sortByRate(cls):
		cls.sortParam='rating'

	# Function to change sort parameter to
	# room availability.
	@classmethod
	def sortByRoomAvailable(cls) :
		cls.sortParam='roomAvl'
	
	def __repr__(self) -> str:
		return "PRHOTELS DATA:\nHotelName:{}\tRoom Available:{}\tLocation:{}\tRating:{}\tPricePer Room:{}".format(self.name,self.roomAvl,self.location,self.rating,self.pricePr)


# Create class for user data.
class User:
	def __init__(self) -> None:
		self.uname=''
		self.uId=0
		self.cost=0

	def __repr__(self) -> str:
		return "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname,self.uId,self.cost)




# Print hotels data.
def PrintHotelData(hotels):
	for h in hotels:
		print(h)


# Sort Hotels data by name.
def SortHotelByName(hotels):
	print("SORT BY NAME:")

	Hotel.sortByName()
	hotels.sort()

	PrintHotelData(hotels)
	print()


# Sort Hotels by rating
def SortHotelByRating(hotels):
	print("SORT BY A RATING:")

	Hotel.sortByRate()
	hotels.sort()
	
	PrintHotelData(hotels)
	print()


# Print Hotels for any city Location.
def PrintHotelBycity(s,hotels):
	print("HOTELS FOR {} LOCATION ARE:".format(s))
	hotelsByLoc=[h for h in hotels if h.location==s]
	
	PrintHotelData(hotelsByLoc)
	print()



# Sort hotels by room Available.
def SortByRoomAvailable(hotels):
	print("SORT BY ROOM AVAILABLE:")
	Hotel.sortByRoomAvailable()
	hotels.sort()
	PrintHotelData(hotels)
	print()


# Print the user's data
def PrintUserData(userName, userId, bookingCost, hotels):
	users=[]
	# Access user data.
	for i in range(3) :
		u=User()
		u.uname = userName[i]
		u.uId = userId[i]
		u.cost = bookingCost[i]
		users.append(u)

	for i in range(len(users)) :
		print(users[i],"\tHotel name:",hotels[i].name)
	


# Functiont to solve
# Hotel Management problem
def HotelManagement(userName,
					userId,
					hotelName,
					bookingCost,
					rooms,
					locations,
					ratings,
					prices):
	# Initialize arrays that stores
	# hotel data and user data
	hotels=[]

	# Create Objects for
	# hotel and user.

	# Initialise the data
	for i in range(3) :
		h=Hotel()
		h.name = hotelName[i]
		h.roomAvl = rooms[i]
		h.location = locations[i]
		h.rating = ratings[i]
		h.pricePr = prices[i]
		hotels.append(h)
	
	print()

	# Call the various operations
	PrintHotelData(hotels)
	SortHotelByName(hotels)
	SortHotelByRating(hotels)
	PrintHotelBycity("Bangalore",
					hotels)
	SortByRoomAvailable(hotels)
	PrintUserData(userName,
				userId,
				bookingCost,
				hotels)


# Driver Code.
if __name__ == '__main__':

	# Initialize variables to stores
	# hotels data and user data.
	userName = ["U1", "U2", "U3"]
	userId = [2, 3, 4] 
	hotelName = ["H1", "H2", "H3"] 
	bookingCost = [1000, 1200, 1100]
	rooms = [4, 5, 6] 
	locations = ["Bangalore",
						"Bangalore",
						"Mumbai"]
	ratings = [5, 5, 3]
	prices = [100, 200, 100] 

	# Function to perform operations
	HotelManagement(userName, userId,
					hotelName, bookingCost,
					rooms, locations,
					ratings, prices)
