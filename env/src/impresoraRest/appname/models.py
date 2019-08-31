from mongoengine import Document, EmbeddedDocument, fields
 
class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)
 
class Tool(Document):
    label = fields.StringField()
    description = fields.StringField()