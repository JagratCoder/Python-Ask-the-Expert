print("Ask the Expert - Capital cities of the World!")
the_world = {}

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def write_to_file(country_name,city_name):
    with open('capital_data.txt','a') as file:
        file.write('\n' + country_name + '/' + city_name)

read_from_file()

while True:
    query_country = input("Type the name of a country? : ")

    if query_country in the_world:
        result = the_world[query_country]
        print(f'The capital city of {query_country} is {result}')

    else:
        new_city =  input(f"What is the capital city of {query_country} ? : ")
        the_world[query_country] = new_city
        write_to_file(query_country,new_city)