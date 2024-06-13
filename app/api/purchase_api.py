from app.settings import settings
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from app.service.purchase import *
from fastapi.responses import JSONResponse
import logging

purchase_api = InferringRouter()

# Initialize logger
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

@cbv(purchase_api)
class Purchase():
    @purchase_api.post('/shop-items')
    async def shop_items(self, user_id: int, item_id: int, qty: int):
        resp = purchase(user_id, item_id, qty)
        if "Error" in resp:
            return JSONResponse(content={"code": 400, "success":False, "message": resp})
        logger.info(f"post /shop-items endpoint is being hit")
        return JSONResponse(content={"code": 200, "success":True, "message": resp})