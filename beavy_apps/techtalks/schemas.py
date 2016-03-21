from beavy.common.paging_schema import makePaginationSchema
from beavy.schemas.object import ObjectField
from marshmallow_jsonapi import Schema, fields

from .models import VIDEO_ID


class VideoSchema(Schema):
    id = fields.Integer()
    created_at = fields.DateTime()
    owner_id = fields.Integer()
    type = fields.String(attribute="discriminator")
    title = fields.String(attribute='title')
    slug = fields.String(attribute='slug')
    description = fields.String(attribute='cooked')

    class Meta:
        type_ = VIDEO_ID  # Required

video = VideoSchema()
video_paged = makePaginationSchema(VideoSchema)()

ObjectField.registry[VIDEO_ID] = VideoSchema
