import asyncio

from logic import create_user, get_users,update_user,get_user_by_id,delete_user

async def main():
    print("""
Select action:
1.Create User
2.Get Users
3.Get Users by ID
4.Update Users
5.Delete USers
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


if __name__ == '__main__':
    asyncio.run(main())