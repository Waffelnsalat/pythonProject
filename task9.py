# Write a Python program to display the examination schedule. (extract the date from exam_st_date)
import datetime

exam_st_date = (11, 12, 2014)

print(str(exam_st_date[0]) + "/" + str(exam_st_date[1]) + "/" + str(exam_st_date[2]))

exam_st_date = (11,12,"test")
print( "The examination will start from : %i / %i / %s"%exam_st_date)