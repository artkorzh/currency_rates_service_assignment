from app.models.schema.base import BaseSchema


class SymbolSchemaBase(BaseSchema):
    symbol: str


class InSymbolSchema(SymbolSchemaBase):
    pass


class SymbolSchema(SymbolSchemaBase):
    id: int


class OutSymbolSchema(SymbolSchema):
    pass
