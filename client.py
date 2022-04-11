import requests

elasticsearch_endpoint = 'https://search.api.hubmapconsortium.org';
portal_index_path = '/portal/search'

def _get_hits(response_json):
    outer_hits = response_json['hits']
    inner_hits = outer_hits['hits']
    return inner_hits


class ApiClient():
    def _request(self, url, body_json=None):
        try:
            response = (
                requests.post(url, headers={}, json=body_json)
                if body_json
                else requests.get(url, headers={})
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        return response.json()

    def get_entity(self, uuid=None):
        query = {'query':
                 {'ids': {'values': [uuid]}}
                 }
        response_json = self._request(
            elasticsearch_endpoint + portal_index_path,
            body_json=query)

        hits = _get_hits(response_json)
        return hits[0]['_source']
