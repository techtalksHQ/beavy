from beavy.models.object import Object
from beavy.common.rendered_text_mixin import RenderedTextMixin
from beavy.common.payload_property import PayloadProperty

# from slugify import slugify_url

VIDEO_ID = "topic"


class Video(Object, RenderedTextMixin):
    __mapper_args__ = {
        'polymorphic_identity': VIDEO_ID
    }

    title = PayloadProperty('title')
    slug = PayloadProperty('slug')
    text = PayloadProperty('text')
    source_url = PayloadProperty('source_url')
    thumbnail_url = PayloadProperty('thumbnail_url')

    CAPABILITIES = [Object.Capabilities.listed, Object.Capabilities.searchable]
