import pykew.powo as powo
from pykew.powo_terms import Name, Filters


#query = { Name.genus: 'Poa', Name.species: 'annua' } # search for species
#query = { Name.kingdom: 'Plantae' }                   # search for kingdom
query = { Name.family: 'Rutaceae' }                   # search for family
#query = { Name.genus: 'Citrus' }                      # search for genus
#query = { Name.rank: 'Family' }                      # search for genus
#query = { Name.genus: '', Name.species: ''  }                   # search for kingdom
#query = { Name.genus: 'Davidia', Name.species: 'involucrata'  }


myfilters = []                                     # gives 400 results for Citrus, 7558 result in Ruraceae; 1,197,433 results with Plantae
#myfilters = [Filters.accepted]                      # gives 32 results for Citrus(includes genus); 2588 result in Ruraceae
#myfilters = [Filters.accepted, Filters.species]     # gives 31 results for Citrus (excludes genus)
myfilters = [Filters.accepted, Filters.genera]       # gives 150 results for Rutaceae  ; 13899 results for kingdom Plantae (=accepted genera in POWO online search)
#myfilters = [Filters.accepted, Filters.genera, Filters.families] # families filer does nothing, e.g. 13899  results for kingdom Plantae
#myfilters = [Filters.accepted, Filters.families]     # 402,409 results; families filer does nothing, e.g. 13899  results for kingdom Plantae
#myfilters = [Filters.families]                       # 1,197,433 results; matches no filters search online at POWO
 

result = powo.search(query, filters = myfilters)


if 1==2:
   print(result.size())
   exit()

for r in result :
   #if 'name' in r : print(r['name'])
   if 'name' in r and 'author' in r : print(r['name']+" "+r['author'])
   #print([line for line in result])

print(result.size())

input()