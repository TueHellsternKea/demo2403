from restcountries import RestCountryApiV2 as rapi

# Get Denmark info
country_list = rapi.get_countries_by_name('Denmark')

# Print information
country = country_list[0]
print(country.name)
print(country.capital)
print(country.calling_codes)
print(country.population)
print(country.flag)
print(country.languages)
