from app.parsers.parser_registry import PARSERS


class DocumentRouter:

    def get_parser(self, document_type):

        parser = PARSERS.get(document_type)

        if parser is None:
            raise ValueError(
                f"No parser registered for {document_type}"
            )

        return parser