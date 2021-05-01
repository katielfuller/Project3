import os.path
def Covid_Cases():
    #initial message
    file = 'county-covid-data.txt'



    file = open(file)
    county_list = []
    read_lines = file.readlines()
    covid_dict = {}
    total_cases = 0
    total_deaths = 0


    for line in read_lines:
        if line[0] != '#':
            split_lines = line.split(',')
            county = split_lines[0]
            confirmed_cases = int(split_lines[1])
            probable_cases = split_lines[2]
            deaths = int(split_lines[3])
            total_cases += confirmed_cases
            total_deaths += deaths



            #adding things to dict and list

            county_list.append(county)
            #names.append('Texas')
            covid_dict[county] = (confirmed_cases, deaths)
            covid_dict['Texas'] = (total_cases, total_deaths)


    file.close()
    return covid_dict, county_list


def Main():
    covid_dict, county_list = Covid_Cases()
    print("Welcome to the Texas Covid Database Dashboard \n\
This provides Covid data in Texas as of 1/26/21. \n\
Creating dictionary from file: ")


    if not os.path.isfile('county-covid-data.txt'):
        print("'File county-covid-data.txt' not found.")
        exit()
    else:
        print(" \nEnter any of the following commands: \n\
Help - list available commands; \n\
Quit - exit this dashboard; \n\
Counties - list all Texas counties; \n\
Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide; \n\
Deaths <countyName>/Texas - Covid deaths in specified county or statewide. \
                                         ")


    while True:
        command = input("\nPlease enter a command: ").lower().split()
        args = command[1:]
        arg = " ".join(args).title()
        elements = 0
        if command[0] == 'help':
            print("Enter any of the following commands: \n\
Help  - list available commands; \n\
Quit - exit this dashboard; \n\
Counties - list all Texas counties; \n\
Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide; \n\
Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")
        elif command[0] == 'counties':
            for county in county_list:

                if elements == 10:

                    elements = 0
                    print()

                print(county, end = ", ")
                elements += 1

        elif command[0] == 'cases':
            if arg in covid_dict.keys():

                print(f"{arg} county has {covid_dict[arg][0]} confirmed Covid cases.")

            elif arg == "texas":
                print(f"Texas total confirmed Covid cases: {covid_dict['Texas'][0]}")

        elif command[0] == 'deaths':

            if arg in covid_dict.keys():
                print(f"{arg} county has {covid_dict[arg][1]} fatalities.")

            elif arg.lower() == 'texas':
                print(f"Texas total confirmed Covid deaths: {covid_dict[Texas][1]}")

        elif command[0] == 'quit':
            print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")
            exit()

        else:
            print("Command is not recognized.  Try again!")



#top_covid_dict, top_county_list = Covid_Cases()

Main()
