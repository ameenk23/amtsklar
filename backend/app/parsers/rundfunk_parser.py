import re
from datetime import datetime

from app.models.domain.rundfunk_document import RundfunkDocument
from app.models.enums import DocumentType
from app.parsers.base_parser import BaseParser


class RundfunkParser(BaseParser):

    def parse(self, text: str) -> RundfunkDocument:

        authority = None
        contribution_number = None
        issue_date = None
        period_start = None
        period_end = None
        amount = None

        # ----------------------------
        # Authority
        # ----------------------------

        if "ARD ZDF Deutschlandradio" in text:
            authority = "ARD ZDF Deutschlandradio Beitragsservice"

        # ----------------------------
        # Contribution Number
        # ----------------------------

        match = re.search(
            r"Beitragsnummer\s+([\d\s]+)",
            text
        )

        if match:
            contribution_number = re.sub(
                r"\D",
                "",
                match.group(1)
            )
        # ----------------------------
        # Issue Date
        # ----------------------------
        match = re.search(
            r"Datum.*?(\d{2}\.\d{2})[.\s]+(\d{4})",
            text,
            re.DOTALL
        )

        print("DATE MATCH:", match)

        if match:
            print(match.group(0))
            print(match.group(1))
            print(match.group(2))

            date_string = f"{match.group(1)}.{match.group(2)}"

            issue_date = datetime.strptime(
                date_string,
                "%d.%m.%Y"
            ).date()

         # ----------------------------
        # Contribution Period
        # ----------------------------
        # ----------------------------
        # Contribution Period
        # ----------------------------

        match = re.search(
            r"(\d{2}\.\d{2}\.\d{4})\s+bis\s+(\d{2}\.\d{2}\.\d{4})",
            text
        )
        print("PERIOD MATCH:", match)

        if match:
            period_start = datetime.strptime(
                match.group(1),
                "%d.%m.%Y"
            ).date()

            period_end = datetime.strptime(
                match.group(2),
                "%d.%m.%Y"
            ).date()
        # ----------------------------
        # Amount
        # ----------------------------

        match = re.search(
            r"(\d+,\d+)\s*EUR",
            text
        )

        if match:

            amount = float(
                match.group(1).replace(",", ".")
            )

        return RundfunkDocument(

            document_type=DocumentType.FESTSETZUNGSBESCHEID,

            authority=authority,

            contribution_number=contribution_number,

            issue_date=issue_date,

            period_start=period_start,

            period_end=period_end,

            amount=amount,
        )