import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from elasticsearch_dsl import Q
from blog.documents import ArticleDocument

"""
Looks up all the articles that:
1) Contain 'language' in the 'title'
2) Don't contain 'ruby' or 'javascript' in the 'title'
3) And contain the query either in the 'title' or 'description'
"""
#query 1
# query = "Loss job phone."
# q = Q(
#      "bool",
#      # must=[
#      #     Q("match", title="language"),
#      # ],
#      # must_not=[
#      #     Q("match", title="ruby"),
#      #     Q("match", title="javascript"),
#      # ],
#      should=[
#          Q("match", title=query),
#          Q("match", description=query),
#      ],
#      minimum_should_match=1)
# search = ArticleDocument.search().query(q)
# response = search.execute()

# query2

query = "I am a developer"  # notice the typo
q = Q(
     "multi_match",
     query=query,
     fields=[
         "title"
     ])
search = ArticleDocument.search().query(q)
response = search.execute()

# print all the hits
for hit in search:
    print(hit.title)


# print all the hits
# for hit in search:
#     print(hit.title)