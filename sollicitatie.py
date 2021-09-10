# sollicitatie Cirscusdirecteur voor Circus HotelDeBotel
# criteria: 
# Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
# In bezit van een Diploma MBO-4 ondernemen
# In bezit van een geldig Vrachtwagen rijbewijs
# In bezit van een hoge hoed
# Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm
# Is langer dan 150 cm
# Is zwaarder dan 90 kg
# Heeft Certificaat “Overleven met gevaarlijk personeel”

import time
import sys

print("""
================================
Sollicitatie "Ruimte Vuilnisman"
================================
""")
time.sleep(1)
# questions
ervaring = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: '))
diploma = {'ja':True, 'nee':False}.get(input('Bent u in bezit van een diploma MBO-4 ondernemen?: ').lower())
rijbewijs = {'ja':True, 'nee':False}.get(input('Bent u in bezit van een geldig vrachtwagen rijbewijs?: ').lower())
hoed = input('Bent u in bezit van een hoge hoge hoed?: ')
lengte = int(input('Wat is uw lichaamslengte in hele cm?: '))
gewicht = int(input('Wat is uw lichaamsgewicht in hele kg?: '))
certificaat = {'ja':True, 'nee':False}.get(input('Bezit u een \"Overleven met gevaarlijk personeel certificaat\"?: ').lower())

geslacht = input('Bent u een man of vrouw?: ').lower()
# booleans
snor = True
haar = True
certificaat = True

if geslacht == 'man':
  snor = {'ja':True, 'nee':False}.get(input('Heeft u een snor breder dan 10cm?: ').lower())
elif geslacht == 'vrouw':
  haar = {'ja':True, 'nee':False}.get(input('Heeft u rood krulhaar langer dan 20 cm?: ').lower())
else:
    print('Helaas hebben we u niet begrepen.')
    sys.exit()

# questions that don't matter
input('Bent u van maandag tot vrijdag beschikbaar?: ')
input('Vul hier 5 slechte en 5 goede punten over jezelf in: ')
input('Kan je goed met collega\'s samenwerken?: ')
input('Werk je liever zelfstandig?: ')



if not all ((snor, haar, certificaat, haar, rijbewijs, diploma, gewicht >= 90, lengte >= 150, ervaring >= 4)):
    print('Helaas voldoet u niet aan de criteria. Het spijt ons!')
    time.sleep(5)
    sys.exit()
else:
  print('U voldoet aan de criteria. Uw sollicitatie is verstuurd.')  