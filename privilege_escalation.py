from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
  "query": {
    "match": {
      "event.action": "sudo"
    }
  }
}

res = es.search(index="filebeat-*", body=query)

if res['hits']['total']['value'] > 5:
    print("Privilege Escalation Detected")