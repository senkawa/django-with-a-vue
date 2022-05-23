import json

from django.http import QueryDict, HttpRequest, HttpResponse

JSON_TYPE = "application/json"


class JSONMiddleware:
    """
    Serializes incoming JSON
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.content_type != JSON_TYPE:
            return self.get_response(request)

        try:
            serialized = json.loads(request.body)

            query = QueryDict("", mutable=True)
            for key, values in serialized.items():
                if isinstance(values, list):
                    for value in values:
                        query.update({key: value})
                else:
                    query.update({key: values})

            if request.method == "GET":
                request.GET = query

            if request.method == "POST":
                request.POST = query

            return self.get_response(request)
        except json.JSONDecodeError:
            return HttpResponse("JSON Decode Error", status=400)
