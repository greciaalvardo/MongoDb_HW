#-------------------------------------------------------------------------
# AUTHOR: Grecia Alvarado
# FILENAME: db_connection_mongo.py
# SPECIFICATION: PyMongo
# FOR: CS 4250- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
from pymongo import MongoClient

def connectDataBase():

    # Create a database connection object using pymongo
    # --> add your Python code here

def createDocument(col, docId, docText, docTitle, docDate, docCat):
    # create a dictionary to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    term_appearances = {}
    terms = docText.lower().split(" ")
    for term in terms:
        term_appearances[term] += 1


    # create a list of dictionaries to include term objects.
    term_objects = []
    for term, count in term_appearances.items():
        d = {'term': term, 'count': count}
        term_objects.append(d)

    #Producing a final document as a dictionary including all the required document fields
    document = {
        'docId': docId,
        'docText': docText,
        'docTitle': docTitle,
        'docDate': docDate,
        'docCat': docCat,
        'terms': term_objects
    }

    # Insert the document
    col.insertOne(document)

def deleteDocument(col, docId):

    # Delete the document from the database
   col.books.deleteOne({'_id': ObjectId(docId) })


def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    col.books.deleteOne({'_id': ObjectId(docId) })

    # Create the document with the same id
    createDocument(col, docId, docText, docTitle, docDate, docCat)

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3'}
    # ...
    # --> add your Python code here