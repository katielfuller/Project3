import os.path
def Covid_Cases():
    #initial message
    file = 'county-covid-data.txt'


    file = open(file, 'r')
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
Creating dictionary from file: county-covid-data.txt ")


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
        command = input("\nPlease enter a command: ").split()
        args = command[1:]
        arg = " ".join(args).title()
        orginal_arg = " ".join(args)
        elements = 0
        if command[0].lower() == 'help':
            print("Help  - list available commands; \n\
Quit - exit this dashboard; \n\
Counties - list all Texas counties; \n\
Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide; \n\
Deaths <countyName>/Texas - Covid deaths in specified county or statewide. \n")
        elif command[0].lower() == 'counties':
            for county in county_list:

                if elements == 10:

                    elements = 0
                    print()

                print(county, end = ", ")

                elements += 1
            print()


        elif command[0].lower() == 'cases':

            if arg == "Texas":
                print(f"Texas total confirmed Covid cases: {covid_dict['Texas'][0]}")

            elif arg in covid_dict.keys():

                print(f"{arg} county has {covid_dict[arg][0]} confirmed Covid cases.")

            else:
                print(f"County {orginal_arg} is not recognized.")

        elif command[0].lower() == 'deaths':

            if arg == 'Texas':
                print(f"Texas total confirmed Covid deaths: {covid_dict['Texas'][1]}")

            elif arg in covid_dict.keys():
                print(f"{arg} county has {covid_dict[arg][1]} fatalities.")

            else:
                print(f"County {original_arg} is not recognized.")

        elif command[0].lower() == 'quit':

            print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")
            exit()

        else:

            print("Command is not recognized.  Try again!")



#top_covid_dict, top_county_list = Covid_Cases()

Main()
