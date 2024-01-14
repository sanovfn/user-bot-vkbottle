from vkbottle.user import User,Message
user = User("vk token") #заменяем на свой токен.
@user.on.message(text='!айди') #команду можно изменить
async def get_user_id(message:Message): 
    user_info = await user.api.users.get(message.reply_message.from_id) #получаем через api в инфу 
    await user.api.messages.edit(peer_id=message.peer_id,message_id=message.get_message_id(),message=f'айди пользователя [id{user_info[0].id}|{user_info[0].first_name} {user_info[0].last_name}]:\n'
                                                                                                     f'{user_info[0].id}') #редачим сообщение с полученной информацией.



user.run_forever()
