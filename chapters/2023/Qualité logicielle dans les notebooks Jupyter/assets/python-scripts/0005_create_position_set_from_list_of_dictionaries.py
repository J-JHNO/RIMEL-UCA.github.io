#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date
from gs_quant.markets.position_set import PositionSet
from gs_quant.session import Environment, GsSession

# In[ ]:


client = 'CLIENT ID'
secret = 'CLIENT SECRET'

GsSession.use(Environment.PROD, client_id=client, client_secret=secret, scopes=('read_product_data',))

# In[ ]:


 # can alternatively specify 'quantity' instead of 'weight'
positions = [
    {'identifier': 'AAPL UW', 'weight': 0.5},
    {'identifier': 'MSFT UW', 'weight': 0.5}
]

# In[ ]:


position_set = PositionSet.from_dicts(positions)
