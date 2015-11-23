import simpleyaml as yaml

data = yaml.load(file("data.yaml","r"))
customers = data['customers']
vipIds = [c['id'] for c in customers if c['vip'] == True]
