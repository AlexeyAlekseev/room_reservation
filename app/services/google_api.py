from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"

async def spreadsheets_create(wrapper_service: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_service.discover("sheets", "v4")
    spreadsheet_body = {
        'properties': {
            'title': f'Отчет на {now_date_time}',
            'locale': 'ru_RU'
        },
        'sheets': [
            {
                'properties': {
                    'sheetType': 'GRID',
                    'sheetId': 0,
                    'title': 'Лист1',
                    'gridProperties': {
                        'rowCount': 100,
                        'columnCount': 11
                    }
                }
            }
        ]
    }
    response = await wrapper_service.as_service_account(
        service.spreadsheets.create(
            json=spreadsheet_body
        )
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid

async def set_user_permissions(
        spreadsheetid: str,
        wrapper_service: Aiogoogle,
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_service.discover("drive", "v3")
    await wrapper_service.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'
        )
    )

async def spreadsheets_update_vlue(
        spreadsheetid: str,
        reservations: list,
        wrapper_service: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_service.discover("sheets", "v4")
    table_values = [
        ['Отчёт от', now_date_time],
        ['Количество регистраций переговорок'],
        ['ID переговорки', 'Кол-во бронирований']
    ]
    for res in reservations:
        now_res = [str(res['meetingroom_id']), str(res['count'])]
        table_values.append(now_res)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    response = await wrapper_service.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetid=spreadsheetid,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )