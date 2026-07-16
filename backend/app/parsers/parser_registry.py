from app.models.enums import DocumentType

from app.parsers.rundfunk_parser import RundfunkParser


PARSERS = {

    DocumentType.FESTSETZUNGSBESCHEID:
        RundfunkParser(),

}