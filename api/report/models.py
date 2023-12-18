from pydantic import BaseModel
from typing import Literal


class shift_report_row_response_model(BaseModel):
    user: int
    shift: int
    transactions: str
    lpn: str = "NOLPN"
    # carteType: Literal['cardtype1', 'cardtype2']
    cardtype: str = 'None'


class shift_report_body_request_model(BaseModel):
    userid: int
    shiftid: int
    transaction: str
    lpn: str = "NOLPN"
    # carteType: Literal['cardtype1', 'cardtype2']
    carteType: str = 'None'
