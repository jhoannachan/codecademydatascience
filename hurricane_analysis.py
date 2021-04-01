# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
updated_damages = []

def conversion_to_float(lst):
  for entry in lst:
    if entry == 'Damages not recorded':
      updated_damages.append(entry)
    elif entry[-1] in conversion.keys():
      new_value = float(entry[:-1])*conversion[entry[-1]]
      updated_damages.append(new_value)
  return updated_damages

print(conversion_to_float(damages))
print(damages)

# 2 
# Create a Table
hurricanes = {}

def construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  for i in range(len(names)):
    hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Death': deaths[i]}
  return hurricanes

# Create and view the hurricanes dictionary

construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)
print(hurricanes['Maria'])

# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key

def hurricane_by_year_dictionary(current_year):
  hurricane_by_year = []
  for name in hurricanes:
    if hurricanes[name]['Year'] == current_year:
      hurricane_by_year.append(hurricanes[name])
  return hurricane_by_year

#test
#print(hurricane_by_year_dictionary(2017))
#print(hurricane_by_year_dictionary(2005))

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

areas_affected = {}
def count_affected_areas(dict):
    for name in dict:
        for area in dict[name]['Areas Affected']:
            if area in areas_affected:
                areas_affected[area] += 1
            else:
                areas_affected[area] = 1
    return areas_affected

print(count_affected_areas(hurricanes))

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in

max_area = 0
def frequently_affected_area(dict):
  max_area_count = 0
  area_name = ''
  for area in dict:
    if dict[area] > max_area_count:
      max_area_count = dict[area]
      area_name = area
  return area_name, max_area_count

print(frequently_affected_area(areas_affected))

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def highest_mortality_hurricane(dict):
  max_mortality = 0
  hurricane_name = ''
  for name in dict:
    if dict[name]['Death'] > max_mortality:
      max_mortality = dict[name]['Death']
      hurricane_name = name
  return hurricane_name, max_mortality

print(highest_mortality_hurricane(hurricanes))

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

def categorize_by_mortality(dict):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for name in dict:
    if dict[name]['Death'] == mortality_scale[0]:
      hurricanes_by_mortality[0].append(name)
    elif mortality_scale[0] < dict[name]['Death'] <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(name)
    elif mortality_scale[1] < dict[name]['Death'] <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(name)
    elif mortality_scale[2] < dict[name]['Death'] <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(name)
    elif mortality_scale[3] < dict[name]['Death'] <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(name)
    else:
      hurricanes_by_mortality[5].append(name)
  return hurricanes_by_mortality

print(categorize_by_mortality(hurricanes))

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def highest_damage_hurricane(dict):
  damage_list = []
  
  hurricane_name = ''
  for name in dict:
    if dict[name]['Damage'] != 'Damages not recorded':
      damage_list.append(dict[name]['Damage'])
  
  max_damage = max(damage_list)

  for name in dict:
        if dict[name]['Damage'] == max_damage:
            return name, max_damage
  
print(highest_damage_hurricane(hurricanes))

# 9
# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key

hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}

def hurricane_damage_rating(dict):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for name in dict:
    if dict[name]['Damage'] == 'Damages not recorded':
      hurricanes_by_damage[0].append(name)
    elif damage_scale[0] < dict[name]['Damage'] <= damage_scale[1]:
      hurricanes_by_damage[1].append(name)
    elif damage_scale[1] < dict[name]['Damage'] < damage_scale[2]:
      hurricanes_by_damage[2].append(name)
    elif damage_scale[2] < dict[name]['Damage'] <= damage_scale[3]:
      hurricanes_by_damage[3].append(name)
    elif damage_scale[3] < dict[name]['Damage'] <= damage_scale[4]:
      hurricanes_by_damage[4].append(name)
    else: 
      hurricanes_by_damage[5].append(name)
  return hurricanes_by_damage

print(hurricane_damage_rating(hurricanes))
