from catalogue.models import Snippet
from django.db.models import Q
from django.conf import settings 
import os 
import sys
tenders = Snippet.objects.filter(Q(is_tender=True) | Q(is_auction=True))
# for t in tenders : 
t = tenders.last()
c =0 
for i, t in enumerate(tenders) : 
	print(i)
	path  = t.image.path

	if os.path.isfile(path):
		print('1 ')
		c+= 1 

	else :
		print('0')
	continue 

print(c)
print(tenders.count())
