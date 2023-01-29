import telebot
import modules.create_inline_buttons as m_inline_button

ipad_bar = telebot.types.InlineKeyboardMarkup()
iphone_bar = telebot.types.InlineKeyboardMarkup()
macbook_bar = telebot.types.InlineKeyboardMarkup()
apple_watch_bar = telebot.types.InlineKeyboardMarkup()
air_pods_bar = telebot.types.InlineKeyboardMarkup()

inline_keyboards = [ipad_bar, iphone_bar, macbook_bar, apple_watch_bar, air_pods_bar]

for inline_keyboard, offer_inline_buttons in zip(inline_keyboards, m_inline_button.buttons):
    inline_keyboard.add(offer_inline_buttons[1], offer_inline_buttons[0])