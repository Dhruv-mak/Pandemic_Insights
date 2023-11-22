import json
import pandas as pd
data = {
    'state_code': [],
    'county_code': [],
    'site_num': [],
    'parameter_code': [],
    'sample_duration': [],
    'sample_duration_code': [],
    'sample_frequency': [],
    'state': [],
    'county': [],
    'date_gmt': [],
    'time_gmt': []
}

with open('final.json') as f:
    d = json.load(f)
    for key, value in d.items():
        if 'state_code' in value:
            data['state_code'].append(value['state_code'])
        else:
            data['state_id'].append(None)
        if 'county_code' in value:
            data['county_code'].append(value['county_code'])
        else:
            data['county_code'].append(None)
        if 'site_number' in value:
            data['site_num'].append(value['site_number'])
        else:
            data['site_num'].append(None)
        if 'parameter_code' in value:
            data['parameter_code'].append(value['parameter_code'])
        else:
            data['parameter_code'].append(None)
        if 'sample_duration' in value:
            data['sample_duration'].append(value['sample_duration'])
        else:
            data['sample_duration'].append(None)
        if 'sample_duration_code' in value:
            data['sample_duration_code'].append(value['sample_duration_code'])
        else:
            data['sample_duration_code'].append(None)
        if 'sample_frequency' in value:
            data['sample_frequency'].append(value['sample_frequency'])
        else:
            data['sample_frequency'].append(None)
        if 'state' in value:
            data['state'].append(value['state'])
        else:
            data['state'].append(None)
        if 'county' in value:
            data['county'].append(value['county'])
        else:
            data['county'].append(None)
        if 'date_gmt' in value:
            data['date_gmt'].append(value['date_gmt'])
        else:
            data['date_gmt'].append(None)
        if 'time_gmt' in value:
            data['time_gmt'].append(value['time_gmt'])
        else:
            data['time_gmt'].append(None)
df = pd.DataFrame(data=data)
df.to_csv('output.csv', index=False)