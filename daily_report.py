from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
count = es.count(index="filebeat-*")

print(f"Total events today: {count['count']}")