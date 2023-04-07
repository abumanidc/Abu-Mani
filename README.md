

Project 1
The project was to extract data from a data set containing data about the top 4000 youtube channels based on subscibers.
The dataset Youtube_dataset was provided which is in csv format.
The 2 requirements of the project was:

1. Use a function to return top 1000 channels and store to a new dataset.
2. To create a new csv file on the system by connecting to the database.

Solution:
Pandas was used in solving this question.
Steps.

Importing pandas library.
Loading csv file to the dataframe.
When importing initially, this step throwed a error, but after specifying the correct encoding the output was obtained.
Data cleaning operations.
head(),columns, size, shape, and dtypes functions were used to clean and analyze the data frame loaded.
Verified whether dataframe is sorted according to the decreasing order of top 4000 subscribers.
Creating function answer1().
The function answer1() performs the following steps:
• Selects the first 1000 rows of a DataFrame named df using the head() method and assigns it to a new DataFrame called df_first1000.
• Value_counts method to calculate the frequency count of unique values in the channeltype column of df_first1000 and assigns it to a variable called ans1.
• Create a new DataFrame named result with two columns: 'Channel Type' and 'Count', where 'Channel Type' contains the unique values of channeltype and 'Count' contains their respective frequency counts from ans1.
• Returns the result DataFrame.
8. Calling the function.
The df_answer_one variable will contain the result of calling the answer1() function, which is a DataFrame with two columns: 'Channel Type' and 'Count'.
9. Cross verifying the resultant dataframe by counting the total data values in df_answer_one dataframe.
Total data values is 962.
Found the total null values in the ‘channeltype’ column of top 1000 youtube channels by subscribers.
10. Loading top 1000 youtube channels by subscribers.
First1000 dataframe was found using head() method.
To_csv() method was used to create the csv file in desktop of the user computer.
11. Importing sqlalchemy and pymysql libraries.
12. Connecting to sql.
13. Loading the top thousand channels using to_sql() method.
14. Dateframe to show the loaded csv in mysql.
