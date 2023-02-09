from combojsonapi.event.resource import EventsResource


class ArticleListEvent(EventsResource):

    def __init__(self):
        self._data_layer = None

    def event_get_publications(self):
        result = {"articles": []}
        for article in self._data_layer.model.query.all():
            result["articles"].append({
                "title": article.title,
                "published": article.created_at
            })
        return result
