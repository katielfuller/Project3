### First Function
1. open the file 'county-covid-data.txt and read it
2. create a list of all the county names
3. create a dictionary with the counties and their confirmed cases and deaths, then add 'Texas' to the end of the dictionary and the total confirmed cases of all the counties and all their deaths
4. close the file
5. return the dictionary and county list
6. create a new function, which will be main  
### Main Code   
7. **print the welcome message:**  
   "Welcome to the Texas Covid Database Dashboard
   This provides Covid data in Texas as of 1/26/21.
   Creating dictionary from file: county-covid-data.txt "
8. **if it's not the 'county-covid-data.txt' file then print the message:**  
   "File county-covid-data.txt' not found.", 
   else print        
   "Enter any of the following commands:  
   Help - list available commands;    
   Quit - exit this dashboard;  
   Counties - list all Texas counties;  
   Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;  
   Deaths <countyName>/Texas - Covid deaths in specified county or statewide."
9. **have a command that says** "Please enter a command: "
10. **you can input help, which prints the message:**  
    "Help  - list available commands;  
    Quit - exit this dashboard;  
    Counties - list all Texas counties;  
    Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;  
    Deaths <countyName>/Texas - Covid deaths in specified county or statewide."
11. the command 'counties' = the list of counties from the first function, 10 counties per line separated by a comma, prof said it's ok is there's a comma after the last county
12. the command 'cases ' followed by a county or Texas returns the confirmed cases. The same thing but with 'deaths'
    if the county does not exist print "County [the county you input] is not recognized."
13. the command 'quit' returns the message "Thank you for using the Texas Covid Database Dashboard.  Goodbye!" and exits out of the command prompt
14. if you input a different command print the messsage "Command is not recognized.  Try again!"
15. if don't input a command, exit out of the command prompt