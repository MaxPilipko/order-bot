import modules.create_bot as m_bot
import modules.offers as m_offers


@m_bot.bot.callback_query_handler(func=lambda callback: callback.data)
def processing_callback(callback):
    manager_chat_id = 709401683 # мой айди для проверки
    
    if "order" in callback.data:
        offer = callback.data.split("order")[1].strip()
        offer = m_offers.offers_dict[offer]
        
        m_bot.bot.send_message(
            callback.message.chat.id,
            " Заказ принят, ожидайте ответа!",
        )
        
        order_title = offer['Title']
        order_url = offer['URL']
        order_img = offer['IMG']
        
        m_bot.bot.send_photo(
            manager_chat_id,
            photo=open(order_img, 'rb'),
            caption=f'Новый заказ\n\nНаименование товара: {order_title}\nURL: {order_url}'
        )