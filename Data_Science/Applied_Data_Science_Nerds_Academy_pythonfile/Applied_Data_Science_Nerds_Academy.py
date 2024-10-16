"""https://www.youtube.com/watch?v=AMtFSAt0tZ0"""


"""Types casting"""
# num = 2

# num1 =float(num)

# print(num1)

# john = False

# print(type(john))

# john1=int(john)

# print(john1)

# print(3*"john")

# name = "john"

# name = name + "is the best"

# print(name)

# print("john is the \n best dancer")
# print("john is the \t best actor")
# print("Michael Jackson \\ is the best") 
# # or
# print(r"Michael Jackson \ is the best")

# A = "Michael Jackson is the best"
# B=A.upper()
# B= A.replace("Michael", "Janet")
# print(B)

"""Find the sub string index"""
# Name = "Michael Jackson"
# Find = Name.find('el')
# print(Find)

"""Tuples"""
# tuple1 = ('disco',10,1.2)
# print(type(tuple1))
# print(tuple1[0])
# # negative index
# print(tuple1[-1])

# tuple2 = tuple1 + ("hard rock",7)
# print(tuple2)

# print(tuple2[0:3])

"""Tuples are immutable"""

# Ratings = (10, 9 ,6,5,10,8,9,6,2)
# Ratings1 = Ratings
# print(Ratings1)
# Ratings = (2,10,1)
# Ratings = Ratings1 + Ratings
# print(Ratings)
# """As the consequense of the immutability we need to create a new variable"""
# RatingsSorted =sorted(Ratings)
# print(RatingsSorted)

"""Tuples: Nesting"""
# NT = (1,2,("pop","rock"),(3,4),("disco",(1,2)))

# print(NT[2][1])

"""LIST
Lists are also ordered sequences
a list is represented with square brackets
list is mutable"""

# List =["Michael Jackson", 10.1,1982,[1,2],('A',1),'MJ']

# print(List[3:5])

# Ratings = [10, 9 ,6,5,10,8,9,6,2]
# Ratings1 = Ratings
# print(Ratings1)
# Ratings = [2,10,1]
# print(Ratings)
# # Ratings1= Ratings+Ratings1
# RatingsSorted =sorted(Ratings1)
# print(RatingsSorted)
# print(Ratings1.extend([Ratings]))
# Ratings.append("A")
# print(Ratings)

# A =["disco",10,1.2]
# A[0]="hard rock"
# print(A)
# del(A[0])
# print(A)

"""CONVERT A LIST TO STRING USING SPLIT"""

# print("hard rock".split())

"""DELIMITER SPLIT"""
# print("A,B,C,D".split(","))

"""MULTIPLE NAMES REFERRING TO THE SAME OBJECT IS KNOWN AS 'ALIASING'"""
# A =["disco",10,1.2]
# B =A
# B[0]="hard rock"
# print(B)
# A[0]="banana"
# print(A)
# """once you have changed the values of A the B values changes as a consequences because both are referring to the same objects """
# print(B)  

"""CLONE THE LIST"""
# A =["disco",10,1.2]
# """clone will keep the copy of the origin list and if the change the A but the B will not affect"""
# B =A[:]
# print(B)
# A[0]="banana"
# print(A)
# print(B)
# """you can use help command to know more about the list"""
# print(help(A))

"""DICTIONARIES"""

# dict ={
#   "Thriller": 1982,
#   "Black in Black":1980,
#   "The Bark Side of the Moon": 1973,
#   "The Bodyguard":1992
# }
# # add
# dict ["Graduatin"]= 2007
# print(dict)
# # delete
# del(dict["Thriller"])
# print(dict)
# # data check
# check = 'The Bodyguard' in dict
# print(check)
# # to see all the keys and values in the dictionary
# print(dict.keys())
# print(dict.values())

"""SETS
sets is also a type of collections
--> this means that like lists and tuples you can input different Python types
Unlike lists and tuples they are unordered
--> This means sets do not record element position
Sets only have unique elements
-->This means there is only one of a particular element in a set
"""

# set1 ={"pop","rock","soul","hard rock","rock","R&B","rock","disco"}
# print(set1)
# # converting list to set
# list=["Michael Jackson", 10.1,1982,('A',1),'MJ']
# set_convert = set(list)
# print(set_convert)

"""list=["Michael Jackson", 10.1, 1982, [1,2], ('A',1), 'MJ']

Strings, numbers, and tuples of immutable elements are hashable and can be added to a set.
Lists and other mutable types are not hashable and cannot be added to a set."""

"""SET OPERATION"""
# set1.add("NSYNC")
# print(set1)
# set1.remove("NSYNC")
# print(set1)
# print("pop" in set1)
# print("john" in set1)

"""SETS MATHEMATICAL SET OPERATIONS"""

""" INTERSECTION OF TWO SETS 
     we use  '&' to define the intersection"""

# set1 ={"pop","rock","soul","hard rock","rock","R&B","rock","disco","AC/DC"}
# set2={10, 9 ,6,5,10,8,9,6,"pop","rock", "AC/DC","balck in black"}
# # this will pick only items that are present in set1 and set2
# intersected_set = set1 & set2
# print(intersected_set)
# # find the union of the sets the results is the new set with all the unique items from both the sets
# print(set1.union(set2))
# # is sub set
# set3 = {"pop","rock"}
# print(set3.issubset(set1))
# set4 = {"pop","rock","black in black"}
# print(set4.issubset(set1))

"""CONDITIONS AND BRANCHING"""

"""LOOPING FOR LIST AND TUPLES"""
"""this is the sytex to itterate through list and which provides the indeces of each elements
   'enumerate' the argument funtion here for the list"""

# squares =["red","yellow","green"]
# for i,square in enumerate(squares):
#     print(f"index= {i}:element= {square}")


"""Python Functions"""

"""SORTED VS SORT"""
# num = [10,7,8,9,4,6,2,3,1,5]
# print(sorted(num))
# print(num)
# """using sorted function it will not effect a exsisting num
#    using sort () exsisting list values gets modified"""
# num.sort()
# print(num)

"""Using 'pass' in functions as a body"""

# def NoWork():
#     pass
# print(NoWork())
# None

# def nowork():
#     pass
#     return None

# def printStuff(Stuff):

#     for i,s in enumerate(Stuff):
#         print("Album",i,"Rating is",s)

# album_ratings = [10.0,8.5,9.5]
# printStuff(album_ratings)

"""TRY... EXCEPT...ELSE...FINALLY STATEMENT EXCEPTION HANDELING"""

# try:
#      getfile = open("myfile", "r")
#      getfile.write("My file for exception handling.")
# except IOError:
#      print("Unable to open or read the data in the file.")

#      """this is not a good pratice and the error should be specified"""
# # except:
# #      print("some other error occurred!")
# else:
#      print("The file was written successfully")
     
#      """since the file is open so we can use the belwo statement to close the file"""
# finally:
#      getfile.close()
#      print("File is now closed.")

"""OBJECTS AND CLASSESS"""

"""In Python every data is an object
   every object has the following:
      > a type
      > an internal data representation(a blueprint)
      > a set of procedres for interaction wit the object(methods)
    
    an object is an instance of a particular type

       """

"""Creating Your Own Types: Defining Classes

   class 
     > Data Attributes
     > Methods"""

# class Circle(object):  

#     def __init__(self, radius, color):
#        self.radius = radius
#        self.color = color
#        print(f"radius = {self.radius} and color = {self.color} of the circle")

#     """usually to order to change the data in an object we define methods in the class"""
#     def add_radius(self,r):
#         self.radius = self.radius +r
#         return(self.radius)
     
# c1=Circle(10, "red")
# # change the data arrtibute
# c1.color = "blue"
# print(c1.color)

# print(c1.add_radius(8))

# """__init__ is the construction of the """


"""READING FILES WITH BUIT-IN OPEN FUNCTION TO CREATE A FILE OBJECT AND OBTAIN THE DATA FROM A TXT FILE"""

# File1 = open("/resources/data/Example2.txt","w") r for reading w for writing and a for appending

# to get the name of the file we can use the attribute "File1.name"

# what mode the object "File1" is in using the data attribute "File1.mode"

# close the file "File1.close()"

"""Opening the file using "with" statement is the better practive because it automatically cloases the file
   all the operation within the indentation block
   you can check the file is closed from outside the indentation
   you can also print the content of the file from the outside 
"""

# """ File Path: The main issue was with the file path. In Python string literals, 
#    backslashes have special meaning. They're used for escape sequences like '\n' for newline. 
#    To fix this, we have two options:
#    a. Use raw strings: r"C:\Users\john1\OneDrive\Code\AI\AI_learnings\Example1.txt"
#    b. Use forward slashes: "C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example1.txt"
#    c. Use os.path.join() as shown in the fixed code, which is the most portable solution.
# """

# with open(r"C:\Users\john1\OneDrive\Code\AI\AI_learnings\Example1.txt","r") as File1:
# with open("C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example1.txt","r") as File1:
# import os
# file_path = os.path.join("C:", "Users", "john1", "OneDrive", "Code", "AI", "AI_learnings", "Example1.txt")
# with open(file_path,"r") as File1:

#     # to read all lines
#     file_stuff=File1.read()
#     print("Entire file content")
#     print(file_stuff)

#     # reset the pointer to beginning
#     File1.seek(0)

#     # read lines
#     file_stuff =File1.readlines()
#     print("\n All lines as a list:")
#     print(file_stuff)

#     # file index (first two line)
#     print("\nFirstline")
#     print( file_stuff[0])
#     print("\nSecondline")
#     print( file_stuff[1])

#     # reset the pointer to beginning
#     File1.seek(0)

#     # read line by line using readline()
#     print("\nReading line by line:")
#     print(File1.readline(), end='')
#     print(File1.readline(), end='')
    
#     # reset the pointer to beginning
#     File1.seek(0)

#     # you can use loop to print out each line
#     print("\n looping")
#     for line in File1:
#         print(line)

#     # reset the pointer to beginning
#     File1.seek(0)
    
#     # no of characters we would like to reaf from a string as an argument 
#     file_stuff =File1.readlines(4)
#     print(file_stuff)

#     File1.seek(0)

#     """Reading Characters: To read a specific number of characters, use read(n) """
#     # Read first 4 characters
#     print("\nFirst 4 characters:")
#     file_stuff = File1.read(4)
#     print(file_stuff)

# print("\nis file closed?",File1.closed)
# print("last read content",file_stuff)

"""Open file and write data to the file"""


# File1 = open("file path","w")
# File1.write("This is line A")

"""using 'with' statement"""
# with open("C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example1.txt","w") as File1:
#    File1.write("This is line A\n")
#    File1.write("This is line B\n")

"""we can write each elements in the list to the file"""
# Lines=["This is line C\n","This is line D\n","This is line E\n","This is line F\n"]
# with open("C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example1.txt","w") as File1:
#  for line in Lines:
#      File1.write(line)
     
"""Appned"""
# with open("C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example1.txt","a") as File1:
#    File1.write("This is line G")

"""Read one file and wirte the data from read file to new file"""

# with open("C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example1.txt","r") as readfile:
#     with open("C:/Users/john1/OneDrive/Code/AI/AI_learnings/Example2.txt","w") as writefile:
        
#         for line in readfile:
#            writefile.write(line)



"""LODAING DATA WITH PANDAS"""

"""dependencies and library are pre written codes to slove problems"""

""" import pandas
    this will load all the build in functions
    read_csv
    Series()
    DataFrame
    values"""

"""open csv file """
# import pandas
# csv_path = 'file1.csv'
# df= pandas.read_csv(csv_path)
# # or
# import pandas as pd
# csv_path = 'file1.csv'
# df =pd.read_csv(csv_path)


"""one way PANDAS allows you to work with data is through DATAFRAMES"""
# import pandas as pd
# csv_path ='file.csv'
# df=pd.read_csv(csv_path)
# df.head()

"""process to read the excel data file using pandas"""
# import pandas as pd
# csv_path ='file.xlsx'
# df=pd.read_excel(xlsx_path)
# df.head()

"""we can create a data frame out of the dictionary
   keys corresponds to column label:
   values list corresponds to rows:"""
# import pandas as pd
# songs ={'Album':['Thriller','Black in Black','The Dark Side of the Moon',\
#                  'The Bodyguard','Bat Out of Hell'],
#         'Released':[1982,1980,1973,1992,1977],
#         'Length':['00:42:19','00:42:11','00:42:49','00:57:44','00:46:33',]}
# # we then cast the dictionary to a data frame using DataFrame
# songs_frame = pd.DataFrame(songs)
# print(songs_frame)

# # we can create a new data frame consist of one coloum'
# df = pd.DataFrame(songs)
# x = df [['Length']]
# print(x)
# # for multiple coloums
# y = df [['Length','Album']]
# print(y)

# # if you want to work with the original dictionary structure:
# z = songs['Released']
# print(z)

"""when we have a data frame we can working with data and save the results in other format
   pandas has a method 'unique' used to find the data unique elements of the data frame"""

# import pandas as pd
# Team ={'Name':['John','Logan','Lokesh','Ivana','John','Ivana','Logan','paul'],
#         'D.O.B':[1977,1980,1973,1992,1977,1983,1992,1993]}

# df = pd.DataFrame(Team)
# u=df['Name'].unique()
# print(u)

# # selecting birth dates after 80s
# x=df['D.O.B']>=1980
# print(x)
"""This will print series of boolen data frames
   if you want to print actual data use the below code"""

# df1 =df[df['D.O.B']>=1980]
# print(df1)
# # df2 =df[['D.O.B']]>=1980
# # print(df2)

"""save the data different formate
   remember to mention the extension"""
# df1.to_csv('D.O.B_after_80s.csv')

"""ONE DIMENSIONAL NUMPY"""

"""NUMPY ARRAY"""

# # Cast a list to numpy array by importing a numpy library
# import numpy as np
# list = [0,1,2,3,4,5,6,7]
# numpyarray =np.array(list)
# print(type(numpyarray))
# # data type
# dataType = numpyarray.dtype
# print(dataType)
# #find data type without coverting to numpy array
# dataType1 = type(list[0])
# print(dataType1)
# # attritubes of numpy array
# print(numpyarray.size)
# # number of array dimensions
# print(numpyarray.ndim)
# # shape is a tupel of interes indicating the size of the array in each dimensions
# print(numpyarray.shape)
# # numpyarray with real numbers
# b = np.array([1,0.1,3.1,.2,213.3])
# print(b.dtype)

"""INDEX AND SLICING OF NUMPY ARRAY"""

# # Change the index value 
# import numpy as np
# c =np.array([20,1,3])
# c[0]=100
# print(c)

"""VECTOR ADDITION AND SUBTRACTION"""

"""It is wiedly used in data science"""

# import numpy as np
# u= [1,0]
# v= [0,1]
# z =[]
# for n, m in zip(u,v):
#     z.append(n+m)
# print(z)

# # numpy vector addtion
# c=np.array(u)
# d=np.array(v)
# add=[c+d]
# print(add)

"""NOTE: ZIP FUNCTION IN PYTHON
   zip is a buit-in-function that allows you to aggregate elements from multiple iterables into a single iterable"""
# names = ['Frankie','Jordan','Alice']
# ages = [30,42,35]

# for employee in zip(names, ages):
#     print(employee)

"""NOTE: ARRAY MULTIPLICATION WITH A SCALAR"""
# import numpy as np
# y =np.array([1,2])
# z=2*y
# print(z)

# # it will required multipl lines of code to performe same operation without numpy
# e= [2,4]
# f=[]
# for i in e:
#     f.append(2*i)
# print(f)

"""NOTE: 'HADAMARD_PRODUCT':PRODUCT OF TWO NUMPY ARRAYS"""
# import numpy as np

# def hadamard_product(matrix_A,matrix_B):
#     if matrix_A.shape != matrix_B.shape:
#       raise ValueError("Both matrices must have the same shape for Hadamard product.")

#     return np.multiply(matrix_A, matrix_B)    
    
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])   

# result = hadamard_product(A,B)
# print(result)

"""NOTE: DOT PRODUCT : is another widely used operation in data science
         dot product is a single number given by the following term and represents how similar two vectors are"""
# import numpy as np
# u=np.array([1,2])
# v=np.array([3,1])
# # 1*3 + 2*1 =5
# result = np.dot(u,v)
# print(result)

"""ADDING CONSTANT TO AN NUMPY ARRAY
   adding constant to an numpy array this property know as 'BROADCASTING'"""
# z=u+1
# print(z)

"""NOTE: UNIVERSAL FUNCTIONS
         is a functions that operates on nd-arrays"""
# #calculating a mean or average value of numpy array using the method mean
# a =np.array([1,-1,1,-1])
# mean_a =a.mean()
# print(mean_a)
# # maxim values
# b =np.array([1,-2,3,4,5])
# max_b = b.max()
# print(max_b)

"""we can use numpy to create functions that map numpy arrays to new numpy arrays"""

# # access the value of pi in numpy
# pi_value =np.pi
# print(pi_value)

# # numpy array in radians this corresponds to x =[0,pi/2,pi]
# x = np.array([0,np.pi/2,np.pi])
# # this corresponds to y= [sin(0),sin(pi/2),sin(pi)]
# y=np.sin(x) 
# # result new array y =[0,1,0]
# print(y)

"""NOTE LINE SPACE:A usesul function for plotting mathematical functions is "LINE SPACE"
        line space returns evenly spaced numbers over specified intervals
         staring point, ending point, num= : no of elements to generate """
# # the space between the samples in 1
# line_space = np.linspace(-2,2,num=5)       
# print(line_space)
# # space between the samples now is 0.5
# line_space1 = np.linspace(-2,2,num=9)
# print(line_space1)


"""PLOTING MATHEMATICAL FUNCTIONS"""
# import numpy as np
# import matplolib.pyplot as plt

# x= np.linspace(0,2*np.pi,10)
# print(x) 
# y= np.sin(x) 
# print(y) 


"""USING NUMPY ARRAY TO CREATE MORE THAN ONE DIMENSION ARRAY"""
"""The Basics and Array creating in 2D
   Indexing and Slicing in 2D
   Basic operation in 2D"""

# # cast the list a with consist of array of lits
# import numpy as np

# a = [[1,2,3,4],[21,23,24,25],[31,34,35,36]]
# A =np.array(a)

# # to access the number of dimension 
# print(A.ndim)

# # attribute shapre return a tuple
# print(A.shape)

# # indexing
# print(A[1][2])
# # slicing a numpy array first two colums
# print(A[0,0:2]) 

# # slicing a numpy array first two rows

# print(A[0:2,2])

"Matrix addition and multiplication is similar to numpy addition and multiplication"

# import numpy as np

# x = np.array([[1,0],[0,1]])
# y = np.array([[2,1],[1,2]])
# z = x+y
# print(z)
# m = 2*z
# print(m)

"""Multiplication of two arrays corresponds his elements wise product """
# p = x * y
# print(p)

""" we can multiply the two matrix of two different size and dimension using np.array.doc()
    In linear algebra the two array should match the colum and row size to preform the operations"""

# A =np.array([[0,1,1],[1,0,1]]   
#            )
# B= np.array([[1,1],[1,1],[-1,1]]
#            )

# C=np.dot(A,B)
# print(C)


"""NOTE:APPLICATION PROGRAMM INTERFACE (API)"""

"""OUTLINE:
   What is an API
   API Libraries
   REST API
     *Request and Response
     *An example with PyCoinGecko"""

# import pandas as pd
# dict = {
#     'a':[11, 21, 31],
#     'b':[12,22,32]
# }
# df = pd.DataFrame(dict)  
# print(df.head())

"""code explaination api lingo:
   instance : df = pd.DataFrame(dict)
   data in the dict passed along through the pandas api 
   when you call the df.head() then the data frame returns the data with heads with first few rows"""

"""NOTE: REST API
   "REprestational State Transfer APIs
   allows you to communication through internet and letting you to take advantage of resources like "storage" and access more data
   "AI ALGORITHUMS" and much more
   In rest api the programm/or you is called as 'client' and the resource/host/server is called as 'web services'
   Client find the service via an 'endpoint'
    
   Set of Rules regarding REST APIs
       * communication
       * Input or Request
       * Output or Response
   
   HTTP methods are a way of transmitting data over the internet
   REST API REQUEST:We tell the rest api what to do by sending a request the request is usally a HTTP message.
   HTTP MESSAGE : Contains a json file
         """
   

"""PyCoinGecko for CoinGecko API"""
"""we will use the pie coin gecko python client or wapper for the coin gecko api 
   we are going to learn pandas time series functions for dealing with time series data
   steps to follow
   pip install pycoingecko and then import the library"""
# import pandas as pd
# from pycoingecko import CoinGeckoAPI
# from datetime import datetime, timedelta
# import plotly.graph_objects as go
# from plotly.offline import plot

# # CLIENT OBJECT
# cg = CoinGeckoAPI()

# # Get current timestamp and timestamp from 30 days ago
# to_timestamp = int(datetime.now().timestamp())  # current time in Unix timestamp
# from_timestamp = int((datetime.now() - timedelta(days=30)).timestamp())  # 30 days ago in Unix timestamp

# #FUNCTION TO REQUEST OUR DATA
# # getting bitcoin data in usd for past 30 days
# bitcoin_data = cg.get_coin_market_chart_range_by_id(id ='bitcoin', vs_currency='usd', from_timestamp=from_timestamp, to_timestamp=to_timestamp )
# # print(bitcoin_data)

# # Extracting the "price" field(which is a list of lists: [[timestamp, price], ...])
# prices = bitcoin_data['prices']

# # Create data frame with 'Timestamp' and 'Price' columns 
# data = pd.DataFrame(prices, columns =['TimeStamp','Price'])
# # print(data)

# # Converting Unix TimeStamp to readable data format
# data['TimeStamp']=pd.to_datetime(data['TimeStamp'],  unit='ms')

# # print the dataframe
# # print(data)  

# # using the above data we want to create the candle stick plot
# candlestick_data = data.groupby(data['TimeStamp'].dt.date).agg({
#     'Price': ['min', 'max','first','last']
# })

# # finally we will use plotly to create the candlestick chart and plot it
# fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index,
#                                     open=candlestick_data['Price']['first'],
#                                     high=candlestick_data['Price']['max'],
#                                     low=candlestick_data['Price']['min'],
#                                     close=candlestick_data['Price']['last'])
#                 ])
                
# fig.update_layout(xaxis_rangeslider_visible =False, 
#                   xaxis_title = 'Date',
#                   yaxis_title= 'Price (USD $)', 
#                   title = 'Bitcoin Candlestick Chart Over Past 30 Days')

# plot(fig, filename = 'bitcoin_candlestick_graph.html')   


"""SIMPLE API'S"""

"""NOTE:WE WILL DISCUSS ABOUT THE APPLICATION PROGAM INTERFACES THAT USE SOME KIND OF AI 
   WE WILL TRANSCRIBE AN AUDIO FILE USING THE WATSON TEXT TO SPEECH API WE WILL THEN TRANSLATE THE TEXT TO A 
   NEW LANGUAGE USING THE WATSON LANGUAGE TANSLATOR
   
   NOTE:Outline:
    *API keys and endpoints
    *Watson Speech to Text
    *Watson Translate
      """   
"API kEYS AND ENDPOINTS"

""""FILE_1_SPEECH TO TEXT"""

# from ibm_watson import SpeechToTextV1

# # service credentials
# url_s2t ="""service endpoint based on the loaciton of services instanse we store the url of the instance "https://stream.watsonplatform.net/speech-to-text/api"""

# # api keys
# iam_apikey_s2t ="desexxxxxxxxxxxxxx9srk"

# # created a speech to text adapter object the parameters are the endpoint and api key
# s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t,url=url_s2t)

# # we have the path of the wave file we would like to convert to text
# filename = 'hello_this_is_python.wav'

# # Create the file object wave with the wav file using open and we set the mode to 'rb' which means to read the file in binary formate
# # the file object allows us access the wav file that contains the audio 
# with open(filename,mode ='rb')as wav:
#    #  we use method recognize from speectotext adaptor object this basically sends the audio file to the endpoint
#    # parameter audio is the file object and content type is the audio formate
#    # service sent respons stored in the object 'response'
#     response = s2t.recognize(audio=wav,content_type ='audio/wav')

#    #  the attribute the result contains a python dictionary we are intrested in key transcript and we assigned to the variable recognized_text
#     response.result
   
#    # recognized_text now contains a string with the transcribed text
#     recognized_text =response.result['results'][0]['alternatives'][0]['transcript']
#     print(recognized_text)

  
"""FILE_2_ LANGUAGE TRANSALTOR"""
"""NOW WE WILL SEE HOW TO USE THE WATSON LANGUAGE TRANSLATOR TO TRANSLATE ENGLISH TO SPANISH"""

# from ibm_watson import LanguageTranslatorV3

# url_lt ='http://gateway.watsonplatform.net/language-translator/api'

# apikey_lt ='ds2xxxxxxxxxxxxxxxasdfcudsi'

# # this api request requires the date of the version
# version_lt='2023-04-09'

# # language translator object
# language_translator = LanguageTranslatorV3(iam_apikey=apikey_lt,url=url_lt,version=version_lt)

# # we can get the list of the languages and that can be indentified as symbols 
# language_translator.list_identifiable_languages().get_result()

# # we can use the method translate this will translate the text the result will be is a detailed responed object
# translation_response = language_translator.translate(text=recognized_text, model_id = 'en-es')
   
# # the result is a dictionary that includes the translation word count and character
# translation = translation_response.get_result()

# spanish_translation =translation['translations'][0]['translation']
# print(spanish_translation)
   
# translation_new = language_translator.translate(text=spanish_translation, model_id ='es-en').get_result()

# translation_eng = translation_new['translations'][0]['translation']
# print(translation_eng)
   
# # translate the text to French as follows
# French_translation = language_translator.translate(text=translation_eng,model_id ='en-fr').get_result()
# French_translation['translations'][0]['translation']


"NOTE:REST APIs WEBSCRAPING AND WORKING WITH FILES"

"""OUTLINE:http
   uniform resource locator:URL
   request
   response
"""
"""HTTP PROTOCOL: 
    This includes many types of REST APIs
   REQUEST MESSAGE:
    example:
    Request Start Line: Get/index.html HTTP/1.0
    Request Header: User-Agent:Python-request/2.21.0
                    Accept-Encoding: gzip, deflate
                    :
    Request bode: "html document"
"""

"""
NOTE:HTTP USING THE REQUEST LIBRARY IN PYTHON
OUTLINE: 
*Request in python
*Get request/post request
   
"""
# import requests
# url ='http://www.ibm.com/'
# r =requests.get(url)
# # request status
# print(r.status_code)
# # request headers
# print(r.request.headers)
# # headers will returns a python dictionary of http response headers
# header =r.headers
# print(header)
# # date of the reqeust send using key data
# print(header['date'])
# # key content_type indicates type of data
# print(header['Content-Type'])
# # encoding using response object r
# print(r.encoding)
# # content type is text and html review frist 100 data
# print(r.text[0:100])
# # request body
# print(r.request.body)

"GET REQUEST WITH URL PARAMETERS"
"""
You can modify the reqeust of your query
GET REQUEST: 
URL:httbin.org/get
BASE URL:httbin.org
ROUTE:/get
NOTE:http://httpbin.org/get? Name =Joseph&ID=123
QUERY STRING:Start of query:?, parameter name: name , value=Joseph,parameter name:ID , value:123

"""
"CREATE QUERY STRING"
# import requests
# # in query string get is appended at the end
# url_get = 'http://httpbin.org/get'

# # to create query string we use payload dictionary
# # keys are the parameter name and values are value of the query string
# payload={"name":"Joseph","ID":"123"}

# # then we pass the dictionary payload to get function
# r=requests.get(url_get,params=payload)
# print(r.url)
# print(r.request.body)
# print(r.status_code)
# print(r.text)
# print(r.headers['Content-Type'])
# print(r.json())
# # the key argus has name and value of the query string
# print(r.json()['args'])

"""NOTE:POST REQUESTS
   POST REQUEST sends the request in request body not in URL
   in post request you will not find any values and paramets"""
# # post URL change the route to post
# url_post = "http://httpbin.org/post"

# payload={"name":"Joseph","ID":"123"}

# r_post = requests.post(url_post,data =payload)

# # compare the POST and Get URL
# print("POST request URL:",r_post.url)
# print("GET request URL:",r.url)

# print("POST request Body:",r_post.request.body)
# print("GET request Body:",r.request.body)

"""NOTE: HTML FOR WEB SCRAPING

OUTLINE:
Reveing the basic HTML of a basic web page
Understand the composition of an HTML Tag
Undersand HTML Trees
Understand HTML Tables"""

"""NOTE: COMPOSITION OF HTML TAG"""

""" NOTE: HTML ANCHOR TAG 
   EXAMPLE : <a href = "https://www.ibm.com">IBM webpage </a>
   it is helpful to think each tag name a class in python and each individual tags are instances
   CONTENT : IBM webpgae
   ATTRIBUTE : <a href = "https://www.ibm.com">
   ATTRIBUTE NAME : href
   ATTRIBUTE VALUE : "https://www.ibm.com" 
"""

"""HTML TREE:HEAD AND BODY"""


"""NOTE: WEBSCRAPING 
OBJECTIVES:
*define webscraping
*beautiful soup objects
*find_all
*webscrape a website

USING PYTHON TO WEBSCRAPING USING TWO MODULES "REQUEST" AND "BEAUTIFUL SOUP" """


"""NOTE: CORRELATION
Measures to what extent different variables are interdependent.
Correlation doesn't imply causation.


"""

