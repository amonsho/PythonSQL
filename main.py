import asyncio

from logic import create_user, get_users,update_user,get_user_by_id,delete_user,create_task
from database import DatabaseConfig

async def main():
    db=DatabaseConfig(
        user='postgres',
        password='Am.on$sh_op',
        db_name='todo'
        )
    await db.connect()
    await db.create_table()

    print("""
Select action:
1.Create User
2.Get Users
3.Get Users by ID
4.Update Users
5.Delete USers
6.Create task
""")
    
    choice = input('Select your choice: ')

    if choice == '1':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        await create_user(username,password)
        print('User is created succsessfully')

    elif choice == '2':
        users = await get_users()
        print(users)

    elif choice == '3':
        user_id = int(input('Enter User ID: '))
        user = await get_user_by_id(user_id)
        print(user)

    elif choice == '4':
        user_id = int(input('Enter USer ID: '))
        new_username = input('Enter new username: ')
        new_password = input('Enter new password: ')
        await update_user(user_id, new_username, new_password)
        print('User update successfully')

    elif choice == '5':
        user_id = int(input('Enter ID to delete: '))
        result= await delete_user(user_id)
        print(result)

    elif choice == '6':
        await create_task(db, 'Go to work', 'I Need Work',7)

if __name__ == '__main__':
    asyncio.run(main())