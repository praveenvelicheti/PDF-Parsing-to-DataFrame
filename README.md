The goal of the project is to extract a table from a PDF and insert it into a SQL Table.

We learn how to extract text from a pdf into a string and manipulate it to seperate the elements of the table from the PDF.
We use the Norman PD arrests data PDF and read the arrests details from a particular day.

We use the following functions to achieve the tasks:

function: fetchincidents(url)
The function takes a url as an argument and downloads the pdf from the url.
We use urllib.requests module to get the file from the input url and write it into a file locally.

function: extractincidents()
The function does not take any argument. The pdf saved locally from the fetchincidents function is read using PyPDF2 module 
and saved as a string. We use the ';' to split rows. Then the  line seperator '\n' is used to distinguish each element of the table.
We combine the Street,City, State to make a single coloumn address.
The function returns a list of lists.

function: createdb()
The function does not take an argument, The function creates a database called normanpd.db and creates a table called arrests inside
it with the following coloumns:

arrest_time,case_number,arrest_location,offense,arrestee_name,arrestee_birthday,arrestee_address,status,officer

function: populatedb()
The function takes in the db file and list of lists. The function inserts values from the list of lists.

function: status()
The function takes the db file as an argument and returns a random row from the database.



