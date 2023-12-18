from pydantic import BaseModel

mydict = {"version": "x.0"}

example_shift_report = [
    {
        '_id': '657a1d5f818a6b9b5100e012',
        'ArticleID': 67895299,
        'lpn': 'FVGHDS4',
        'price': 123.79,
        'carteType': 'Short Term Parker',
        'duration': '4h'
    },
    {
        '_id': '657a23682a7456ffc0f18213 ',
        'ArticleID': 4522555,
        'lpn': 'Fatmaa',
        'price': 1000,
        'carteType': 'Long Term Parker',
        'duration': '8h',
        'connection': 'abncbcv'
    }
]


class shift_report_row(BaseModel):
    ArticleID: int
    lpn: str = 'NOLPN'
    price: float
    carteType: str
    duration: str
