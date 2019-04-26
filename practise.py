from vega_datasets import data
import altair

data = altair.topo_feature(r'data\districts.json',feature='nepal')

dict = data.to_dict()

for key in dict.items():
    print key