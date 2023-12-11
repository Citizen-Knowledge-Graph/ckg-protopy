from pyshacl import validate
from pyshacl.rdfutil import load_from_source

data_graph = load_from_source('db/profiles/citizen-a.ttl')
sg = load_from_source('db/queries/citizen-solar-funding.ttl')

r = validate(data_graph,
             shacl_graph=sg,
             allow_infos=True,
             allow_warnings=True
             )
print(r)
