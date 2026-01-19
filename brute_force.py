from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
  "query": {
    "match": {
      "event.action": "failed-login"
    }
  }
}

res = es.search(index="filebeat-*", body=query)

if res['hits']['total']['value'] > 10:
    print("Brute Force Attack Detected")