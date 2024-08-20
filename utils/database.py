import aiomysql

async def connectDB():
    connect = await aiomysql.connect(
        host='localhost',
        port=3306,
        user='sattorbek',
        password='sattorbek22',
        db='telegram_bot'
    )
    return connect

async def add_user(user_id, language):
    connect = await connectDB()
    async with connect.cursor() as cursor:
        await cursor.execute(
            'INSERT INTO users (user_id, language) VALUES (%s, %s) ON DUPLICATE KEY UPDATE language = VALUES(language);',
            (user_id, language)
        )
        await connect.commit()
    connect.close()

async def update_user(user_id, language):
    connect = await connectDB()
    async with connect.cursor() as cursor:
        await cursor.execute(
            'UPDATE users SET language = %s WHERE user_id = %s',
            (language, user_id)
        )
        await connect.commit()
    connect.close()

async def create_table():
    connect = await connectDB()
    async with connect.cursor() as cursor:
        await cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(255) UNIQUE,
                language VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        await connect.commit()
    connect.close()

