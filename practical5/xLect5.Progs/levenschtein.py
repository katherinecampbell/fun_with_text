__author__ = 'user'

from nltk.metrics import distance as dist


#  transposition flag allows transpositions edits (e.g., â€œabâ€� -> â€œbaâ€�),

s1 = 'dr mark keane'
s2 = 'mr mark bean'

s3 = 'rain'
s4 = 'shine'

s5 = 'mr rowan atkinson'
s6 = 'mr bean'

ans = dist.edit_distance(s1, s2, transpositions=False)
print(ans)

ans = dist.edit_distance(s3, s4, transpositions=False)
print(ans)

ans = dist.edit_distance(s5, s6, transpositions=False)
print(ans)

ans = dist.levenschtein(s1, s2)
print(ans)

ans = dist.levenschtein(s3, s4)
print(ans)

ans = dist.levenschtein(s5, s6)
print(ans)
