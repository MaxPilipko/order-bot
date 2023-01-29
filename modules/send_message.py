import modules.create_inline_keyboard as m_inline_keyboard
import modules.create_bot as m_bot
import modules.create_buttons as m_button
import modules.offers as m_offers

def send_message(message):
    if message.text == m_button.new_btn.text \
    or message.text == m_button.sale_btn.text \
    or message.text == m_button.discount_btn.text:
        for offer, inline_keyboard in zip(m_offers.offers, m_inline_keyboard.inline_keyboards):
            m_bot.bot.send_photo(
                message.chat.id,
                open(offer['IMG'], "rb"),
                offer['Title'],
                reply_markup=inline_keyboard
            )