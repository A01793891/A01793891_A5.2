#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
from typing import Any, Hashable, Iterable, Optional
import pandas as pd
# In[2]:

# In[3]:

in_put0 = open('/Users/andrei/Desktop/Ejercicio2/TC1.ProductList.json', encoding="utf-8")

json_decode = json.load(in_put0)

result = []

for item in json_decode:
    my_dict = {}
    my_dict['title'] = item.get('title')
    my_dict['price'] = item.get('price')
    result.append(my_dict)


# In[4]:


Results = pd.DataFrame(result)


# In[5]:

def buscar_dicc(it_case: Iterable[dict], clave: Hashable,
                valor: Any) -> Optional[dict]:
    for dicc in it_case:
        if dicc[clave] == valor:
            return dicc
        else:
            dicc[clave] != valor
    return {'title': 'not found', 'price': 0.0}


# In[6]:


buscar_dicc(result, "title", "Basil")


# In[7]:


buscar_dicc(result, "title", "Frijoles")


# In[8]:

in_put1 = open('/Users/andrei/Desktop/Ejercicio2/TC1.Sales.json', encoding="utf-8")
json_decode = json.load(in_put1)

result1 = []
for item in json_decode:
    my_dict = {}
    my_dict['Product'] = item.get('Product')
    my_dict['Quantity'] = item.get('Quantity')
    result1.append(my_dict)


# In[9]:


in_put2 = open('/Users/andrei/Desktop/Ejercicio2/TC2.Sales.json', encoding="utf-8")
json_decode = json.load(in_put2)

result2 = []

for item in json_decode:
    my_dict = {}
    my_dict['Product'] = item.get('Product')
    my_dict['Quantity'] = item.get('Quantity')
    result2.append(my_dict)


# In[10]:


in_put3 = open('/Users/andrei/Desktop/Ejercicio2/TC3.Sales.json', encoding="utf-8")
json_decode = json.load(in_put3)

result3 = []

for item in json_decode:
    my_dict = {}
    my_dict['Product'] = item.get('Product')
    my_dict['Quantity'] = item.get('Quantity')
    result3.append(my_dict)


# In[11]:


consumoTC1 = pd.DataFrame.from_dict(result1)


# In[12]:


consumoTC2 = pd.DataFrame.from_dict(result2)


# In[13]:


consumoTC3 = pd.DataFrame.from_dict(result3)


# In[14]:


producto0 = consumoTC1['Product'].iloc[0]
producto1 = consumoTC1['Product'].iloc[1]
producto2 = consumoTC1['Product'].iloc[2]
producto3 = consumoTC1['Product'].iloc[3]
producto4 = consumoTC1['Product'].iloc[4]
producto5 = consumoTC1['Product'].iloc[5]
producto6 = consumoTC1['Product'].iloc[6]
producto7 = consumoTC1['Product'].iloc[7]
producto8 = consumoTC1['Product'].iloc[8]
producto9 = consumoTC1['Product'].iloc[9]
producto10 = consumoTC1['Product'].iloc[10]
producto11 = consumoTC1['Product'].iloc[11]
producto12 = consumoTC1['Product'].iloc[12]
producto13 = consumoTC1['Product'].iloc[13]
producto14 = consumoTC1['Product'].iloc[14]
producto15 = consumoTC1['Product'].iloc[15]
producto16 = consumoTC1['Product'].iloc[16]
producto17 = consumoTC1['Product'].iloc[17]
producto18 = consumoTC1['Product'].iloc[18]
producto19 = consumoTC1['Product'].iloc[19]
producto20 = consumoTC1['Product'].iloc[20]
producto21 = consumoTC1['Product'].iloc[21]
producto22 = consumoTC1['Product'].iloc[22]
producto23 = consumoTC1['Product'].iloc[23]
producto24 = consumoTC1['Product'].iloc[24]
producto25 = consumoTC1['Product'].iloc[25]
producto26 = consumoTC1['Product'].iloc[26]
producto27 = consumoTC1['Product'].iloc[27]
producto28 = consumoTC1['Product'].iloc[28]
producto29 = consumoTC1['Product'].iloc[29]
producto30 = consumoTC1['Product'].iloc[30]
producto31 = consumoTC1['Product'].iloc[31]
producto32 = consumoTC1['Product'].iloc[32]
producto33 = consumoTC1['Product'].iloc[33]
producto34 = consumoTC1['Product'].iloc[34]
producto35 = consumoTC1['Product'].iloc[35]
producto36 = consumoTC1['Product'].iloc[36]
producto37 = consumoTC1['Product'].iloc[37]
producto38 = consumoTC1['Product'].iloc[38]
producto39 = consumoTC1['Product'].iloc[39]
producto40 = consumoTC1['Product'].iloc[40]
producto41 = consumoTC1['Product'].iloc[41]
producto42 = consumoTC1['Product'].iloc[42]
producto43 = consumoTC1['Product'].iloc[43]
producto44 = consumoTC1['Product'].iloc[44]
producto45 = consumoTC1['Product'].iloc[45]


# In[15]:

precio = pd.DataFrame(
    [buscar_dicc(result, "title", producto0),
     buscar_dicc(result, "title", producto1),
     buscar_dicc(result, "title", producto2),
     buscar_dicc(result, "title", producto3),
     buscar_dicc(result, "title", producto4),
     buscar_dicc(result, "title", producto5),
     buscar_dicc(result, "title", producto6),
     buscar_dicc(result, "title", producto7),
     buscar_dicc(result, "title", producto8),
     buscar_dicc(result, "title", producto9),
     buscar_dicc(result, "title", producto10),
     buscar_dicc(result, "title", producto11),
     buscar_dicc(result, "title", producto12),
     buscar_dicc(result, "title", producto13),
     buscar_dicc(result, "title", producto14),
     buscar_dicc(result, "title", producto15),
     buscar_dicc(result, "title", producto16),
     buscar_dicc(result, "title", producto17),
     buscar_dicc(result, "title", producto18),
     buscar_dicc(result, "title", producto19),
     buscar_dicc(result, "title", producto20),
     buscar_dicc(result, "title", producto21),
     buscar_dicc(result, "title", producto22),
     buscar_dicc(result, "title", producto23),
     buscar_dicc(result, "title", producto24),
     buscar_dicc(result, "title", producto25),
     buscar_dicc(result, "title", producto26),
     buscar_dicc(result, "title", producto27),
     buscar_dicc(result, "title", producto28),
     buscar_dicc(result, "title", producto29),
     buscar_dicc(result, "title", producto30),
     buscar_dicc(result, "title", producto31),
     buscar_dicc(result, "title", producto32),
     buscar_dicc(result, "title", producto33),
     buscar_dicc(result, "title", producto34),
     buscar_dicc(result, "title", producto35),
     buscar_dicc(result, "title", producto36),
     buscar_dicc(result, "title", producto37),
     buscar_dicc(result, "title", producto38),
     buscar_dicc(result, "title", producto39),
     buscar_dicc(result, "title", producto40),
     buscar_dicc(result, "title", producto41),
     buscar_dicc(result, "title", producto42),
     buscar_dicc(result, "title", producto43),
     buscar_dicc(result, "title", producto44),
     buscar_dicc(result, "title", producto45)])


# In[16]:


calculoTC1 = precio['price']*consumoTC1['Quantity']


# In[17]:


# In[18]:


TC1 = calculoTC1.sum()


# In[19]:


product0 = consumoTC2['Product'].iloc[0]
product1 = consumoTC2['Product'].iloc[1]
product2 = consumoTC2['Product'].iloc[2]
product3 = consumoTC2['Product'].iloc[3]
product4 = consumoTC2['Product'].iloc[4]
product5 = consumoTC2['Product'].iloc[5]
product6 = consumoTC2['Product'].iloc[6]
product7 = consumoTC2['Product'].iloc[7]
product8 = consumoTC2['Product'].iloc[8]
product9 = consumoTC2['Product'].iloc[9]
product10 = consumoTC2['Product'].iloc[10]
product11 = consumoTC2['Product'].iloc[11]
product12 = consumoTC2['Product'].iloc[12]
product13 = consumoTC2['Product'].iloc[13]
product14 = consumoTC2['Product'].iloc[14]
product15 = consumoTC2['Product'].iloc[15]
product16 = consumoTC2['Product'].iloc[16]
product17 = consumoTC2['Product'].iloc[17]
product18 = consumoTC2['Product'].iloc[18]
product19 = consumoTC2['Product'].iloc[19]
product20 = consumoTC2['Product'].iloc[20]
product21 = consumoTC2['Product'].iloc[21]
product22 = consumoTC2['Product'].iloc[22]
product23 = consumoTC2['Product'].iloc[23]
product24 = consumoTC2['Product'].iloc[24]
product25 = consumoTC2['Product'].iloc[25]
product26 = consumoTC2['Product'].iloc[26]
product27 = consumoTC2['Product'].iloc[27]
product28 = consumoTC2['Product'].iloc[28]
product29 = consumoTC2['Product'].iloc[29]
product30 = consumoTC2['Product'].iloc[30]
product31 = consumoTC2['Product'].iloc[31]
product32 = consumoTC2['Product'].iloc[32]
product33 = consumoTC2['Product'].iloc[33]
product34 = consumoTC2['Product'].iloc[34]
product35 = consumoTC2['Product'].iloc[35]
product36 = consumoTC2['Product'].iloc[36]
product37 = consumoTC2['Product'].iloc[37]
product38 = consumoTC2['Product'].iloc[38]
product39 = consumoTC2['Product'].iloc[39]
product40 = consumoTC2['Product'].iloc[40]
product41 = consumoTC2['Product'].iloc[41]
product42 = consumoTC2['Product'].iloc[42]
product43 = consumoTC2['Product'].iloc[43]
product44 = consumoTC2['Product'].iloc[44]
product45 = consumoTC2['Product'].iloc[45]
# In[20]:

precioTC2 = pd.DataFrame(
    [buscar_dicc(result, "title", product0),
     buscar_dicc(result, "title", product1),
     buscar_dicc(result, "title", product2),
     buscar_dicc(result, "title", product3),
     buscar_dicc(result, "title", product4),
     buscar_dicc(result, "title", product5),
     buscar_dicc(result, "title", product6),
     buscar_dicc(result, "title", product7),
     buscar_dicc(result, "title", product8),
     buscar_dicc(result, "title", product9),
     buscar_dicc(result, "title", product10),
     buscar_dicc(result, "title", product11),
     buscar_dicc(result, "title", product12),
     buscar_dicc(result, "title", product13),
     buscar_dicc(result, "title", product14),
     buscar_dicc(result, "title", product15),
     buscar_dicc(result, "title", product16),
     buscar_dicc(result, "title", product17),
     buscar_dicc(result, "title", product18),
     buscar_dicc(result, "title", product19),
     buscar_dicc(result, "title", product20),
     buscar_dicc(result, "title", product21),
     buscar_dicc(result, "title", product22),
     buscar_dicc(result, "title", product23),
     buscar_dicc(result, "title", product24),
     buscar_dicc(result, "title", product25),
     buscar_dicc(result, "title", product26),
     buscar_dicc(result, "title", product27),
     buscar_dicc(result, "title", product28),
     buscar_dicc(result, "title", product29),
     buscar_dicc(result, "title", product30),
     buscar_dicc(result, "title", product31),
     buscar_dicc(result, "title", product32),
     buscar_dicc(result, "title", product33),
     buscar_dicc(result, "title", product34),
     buscar_dicc(result, "title", product35),
     buscar_dicc(result, "title", product36),
     buscar_dicc(result, "title", product37),
     buscar_dicc(result, "title", product38),
     buscar_dicc(result, "title", product39),
     buscar_dicc(result, "title", product40),
     buscar_dicc(result, "title", product41),
     buscar_dicc(result, "title", product42),
     buscar_dicc(result, "title", product43),
     buscar_dicc(result, "title", product44),
     buscar_dicc(result, "title", product45)])


# In[21]:


calculoTC2 = precioTC2['price']*consumoTC2['Quantity']


# In[22]:


TC2 = calculoTC2.sum()


# In[23]:


produc0 = consumoTC3['Product'].iloc[0]
produc1 = consumoTC3['Product'].iloc[1]
produc2 = consumoTC3['Product'].iloc[2]
produc3 = consumoTC3['Product'].iloc[3]
produc4 = consumoTC3['Product'].iloc[4]
produc5 = consumoTC3['Product'].iloc[5]
produc6 = consumoTC3['Product'].iloc[6]
produc7 = consumoTC3['Product'].iloc[7]
produc8 = consumoTC3['Product'].iloc[8]
produc9 = consumoTC3['Product'].iloc[9]
produc10 = consumoTC3['Product'].iloc[10]
produc11 = consumoTC3['Product'].iloc[11]
produc12 = consumoTC3['Product'].iloc[12]
produc13 = consumoTC3['Product'].iloc[13]
produc14 = consumoTC3['Product'].iloc[14]
produc15 = consumoTC3['Product'].iloc[15]
produc16 = consumoTC3['Product'].iloc[16]
produc17 = consumoTC3['Product'].iloc[17]
produc18 = consumoTC3['Product'].iloc[18]
produc19 = consumoTC3['Product'].iloc[19]
produc20 = consumoTC3['Product'].iloc[20]
produc21 = consumoTC3['Product'].iloc[21]
produc22 = consumoTC3['Product'].iloc[22]
produc23 = consumoTC3['Product'].iloc[23]
produc24 = consumoTC3['Product'].iloc[24]
produc25 = consumoTC3['Product'].iloc[25]
produc26 = consumoTC3['Product'].iloc[26]
produc27 = consumoTC3['Product'].iloc[27]
produc28 = consumoTC3['Product'].iloc[28]
produc29 = consumoTC3['Product'].iloc[29]
produc30 = consumoTC3['Product'].iloc[30]
produc31 = consumoTC3['Product'].iloc[31]
produc32 = consumoTC3['Product'].iloc[32]
produc33 = consumoTC3['Product'].iloc[33]
produc34 = consumoTC3['Product'].iloc[34]
produc35 = consumoTC3['Product'].iloc[35]
produc36 = consumoTC3['Product'].iloc[36]
produc37 = consumoTC3['Product'].iloc[37]
produc38 = consumoTC3['Product'].iloc[38]
produc39 = consumoTC3['Product'].iloc[39]
produc40 = consumoTC3['Product'].iloc[40]
produc41 = consumoTC3['Product'].iloc[41]
produc42 = consumoTC3['Product'].iloc[42]
produc43 = consumoTC3['Product'].iloc[43]
produc44 = consumoTC3['Product'].iloc[44]
produc45 = consumoTC3['Product'].iloc[45]


# In[24]:


precioTC3 = pd.DataFrame(
    [buscar_dicc(result, "title", product0),
     buscar_dicc(result, "title", produc1),
     buscar_dicc(result, "title", produc2),
     buscar_dicc(result, "title", produc3),
     buscar_dicc(result, "title", produc4),
     buscar_dicc(result, "title", produc5),
     buscar_dicc(result, "title", produc6),
     buscar_dicc(result, "title", produc7),
     buscar_dicc(result, "title", produc8),
     buscar_dicc(result, "title", produc9),
     buscar_dicc(result, "title", produc10),
     buscar_dicc(result, "title", produc11),
     buscar_dicc(result, "title", produc12),
     buscar_dicc(result, "title", produc13),
     buscar_dicc(result, "title", produc14),
     buscar_dicc(result, "title", produc15),
     buscar_dicc(result, "title", produc16),
     buscar_dicc(result, "title", produc17),
     buscar_dicc(result, "title", produc18),
     buscar_dicc(result, "title", produc19),
     buscar_dicc(result, "title", produc20),
     buscar_dicc(result, "title", produc21),
     buscar_dicc(result, "title", produc22),
     buscar_dicc(result, "title", produc23),
     buscar_dicc(result, "title", produc24),
     buscar_dicc(result, "title", produc25),
     buscar_dicc(result, "title", produc26),
     buscar_dicc(result, "title", produc27),
     buscar_dicc(result, "title", produc28),
     buscar_dicc(result, "title", produc29),
     buscar_dicc(result, "title", produc30),
     buscar_dicc(result, "title", produc31),
     buscar_dicc(result, "title", produc32),
     buscar_dicc(result, "title", produc33),
     buscar_dicc(result, "title", produc34),
     buscar_dicc(result, "title", produc35),
     buscar_dicc(result, "title", produc36),
     buscar_dicc(result, "title", produc37),
     buscar_dicc(result, "title", produc38),
     buscar_dicc(result, "title", produc39),
     buscar_dicc(result, "title", produc40),
     buscar_dicc(result, "title", produc41),
     buscar_dicc(result, "title", produc42),
     buscar_dicc(result, "title", produc43),
     buscar_dicc(result, "title", produc44),
     buscar_dicc(result, "title", produc45)])


# In[25]:


calculoTC3 = precioTC3['price']*consumoTC3['Quantity']


# In[26]:


TC3 = calculoTC3.sum()


# In[27]:


Total = pd.DataFrame([TC1, TC2, TC3])


# In[28]:


Total.columns = ['Total']


# In[29]:


Total.index = ['TC1', 'TC2', 'TC3']


# In[31]:

print(Total)

# In[44]:


Total.to_csv('SalesResults', sep='\t')


# In[ ]:
