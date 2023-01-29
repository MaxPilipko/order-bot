import modules.create_bot as m_bot
import modules.create_keyboard as m_keyboard
import modules.send_message as m_send_message

@m_bot.bot.message_handler(commands=['start'])
def start(message):
    first_name = message.chat.first_name
    username = message.chat.username
    name = username if username else first_name
    
    m_bot.bot.send_photo(
        chat_id=message.chat.id,
        photo=open('images\\hello.jpg', 'rb'),
        caption=f"Привет, {name}! Рады тебя видеть в нашем магазине",
        reply_markup=m_keyboard.start_bar
    )
    
    m_bot.bot.register_next_step_handler(
        message, 
        m_send_message.send_message
    )