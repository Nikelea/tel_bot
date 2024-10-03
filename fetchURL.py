import aiohttp



async def fetch_currency():
    url = "https://currate.ru/api/?get=rates&pairs=USDRUB&key=a474f3379ded8011d3f71d0d9e9af027"
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; TelegramBot/1.0)',
        'Accept': 'application/json',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                try:
                    data = await response.json(content_type=None)
                    return data.get('data', 'Не удалось получить данные.')
                except aiohttp.ContentTypeError:
                    text_response = await response.text()
                    return f"Ожидался JSON, но получен HTML: {text_response}"
            else:
                return "Ошибка при получении данных с сервера."
