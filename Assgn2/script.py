# https://en.wikipedia.org/wiki/User:Rockarya2001/sandbox    (link to sandbox)
import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import pywikibot

endpoint_url = "https://query.wikidata.org/sparql"

# the file name in which all the sentences would be written
file_name = 'hindi_lang.txt'

# clearing the file before writing
open(file_name, "w").close()

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def id_to_text(id):
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, id)
    item_dict = item.get()
    # used english value if hindi version is not present
    return_value = item_dict['labels']['en']
    if item_dict['labels'].get('hi') != None:
          return_value = item_dict['labels']['hi']
          
    return return_value

def write_to_file(text):
    print(text)
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')   


# GENERALIZATON
# this is id of Narendra Modi
pm_id = 'Q1058'   #just replace this id with the id of the prime minister for whom u want to generate information
pm_name = id_to_text(pm_id)

query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{ ?a wdt:P6 wd:""" + pm_id + """.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""

results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text =  pm_name + ' ' + val + ' के प्रधानमंत्री हैं।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P551 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = val + ' पर ' + pm_name + ' रहते हैं।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P569 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = pm_name + ' का जन्म ' + val + ' को हुआ था।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P19 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = pm_name + ' का जन्म ' + val + ' में हुआ था।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P22 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = val + ', ' + pm_name + ' के पिता हैं।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P25 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = val + ', ' + pm_name + ' की मां हैं।'
write_to_file(text)

query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P26 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = val + ', ' + pm_name + ' की पत्नी हैं।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription 
WHERE
{
  wd:""" + pm_id + """ wdt:P2048 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = pm_name + ' की ऊंचाई ' + val + ' मीटर है।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription 
WHERE
{
  wd:""" + pm_id + """ wdt:P2067 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text =  pm_name + ' का वजन ' + val + ' किलो है।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription 
WHERE
{
  wd:""" + pm_id + """ wdt:P140 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text =  pm_name + ' ' + val + ' के है।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription 
WHERE
{
  wd:""" + pm_id + """ wdt:P2218 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text =  pm_name + ' की कुल संपत्ति ' + val + ' डॉलर है।'
write_to_file(text)


query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P102 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    break

text = pm_name + ' ' + val + ' के सदस्य हैं।'
write_to_file(text)

        
    
# Education
query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P69 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    write_to_file(val)


# significant events
query = """
SELECT ?a ?aLabel ?aDescription 
WHERE
{
  wd:""" + pm_id + """ wdt:P793 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    write_to_file(val)    
    

# positions held
query = """
SELECT ?a ?aLabel ?aDescription
WHERE
{
  wd:""" + pm_id + """ wdt:P39 ?a.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "hi". }
}
"""
results = get_results(endpoint_url, query)
val = ''
for result in results["results"]["bindings"]:
    val = result['aLabel']['value']
    write_to_file(val)    