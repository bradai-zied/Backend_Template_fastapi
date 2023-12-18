from fastapi import HTTPException, Request, status, APIRouter
from config.log_config import logger
from api.report.logic import example_shift_report
from api.report.models import shift_report_row_response_model, shift_report_body_request_model
from database.models.report import Report_document, Order, Item

reportrouter = APIRouter(prefix='/report')


@reportrouter.get("/version")
def xx():
    # I1 = Item(name="zvo", price=5000)
    # I1.save()
    # I1_id = I1.id
    # print(I1_id)
    # Order.objects(id='657c956409930d9b2d541ac4').update_one(push__items=I1)
    # o1 = Order(order_number='abcd')
    # o1.save()
    print(Order.objects.get(id='657c956409930d9b2d541ac4').to_mongo().to_dict())
    return 'mydict'


@reportrouter.get("/shift_report", response_model=list[shift_report_row_response_model])
def xxx(userid: int):
    try:
        documents = Report_document.objects(user=userid)
        logger.info(f'is={userid} found :{documents.count()} document')
        logger.debug(f'is={userid} found :{documents}')
        retlist = [shift_report_row_response_model(
            **document.to_mongo()) for document in documents]
    except Exception as Ex:
        raise HTTPException(status=500, details=f' error {Ex} ')
        # print('An exception occurred')
    logger.debug(f'is={userid} found :{documents.count()}')
    return retlist


@reportrouter.post("/shift_report")
def apcds(RequestBody: shift_report_body_request_model, request: Request):
    R1 = Report_document(user=str(RequestBody.userid),
                         shift=RequestBody.shiftid,
                         clientip=request.client.host
                         )
    R1.save()
    return 'hello'
