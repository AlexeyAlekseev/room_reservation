from datetime import datetime

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser

from app.crud.reservation import reservation_crud
from app.services.google_api import spreadsheets_create, set_user_permissions, \
    spreadsheets_update_vlue

router = APIRouter()

@router.post(
    '/',
    response_model=list[dict[str, str]],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        from_reserve: datetime,
        to_reserve: datetime,
        session: AsyncSession = Depends(get_async_session),
        wrapper_service: Aiogoogle = Depends(get_service),
):
    """Только для суперюзеров."""
    reservations = await reservation_crud.get_count_res_at_the_same_time(
        from_reserve, to_reserve, session
    )
    spreadsheetsid = await spreadsheets_create(wrapper_service)
    await set_user_permissions(spreadsheetsid, wrapper_service)
    await spreadsheets_update_vlue(
        spreadsheetsid, reservations, wrapper_service
    )
    return reservations