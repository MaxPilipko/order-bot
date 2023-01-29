import telebot
import modules.urls as m_urls

ipad_web_btn = telebot.types.InlineKeyboardButton(text="Перейти на сайт", url=m_urls.ipad)
ipad_order_btn = telebot.types.InlineKeyboardButton(text="Заказать", callback_data="order ipad")

iphone_web_btn = telebot.types.InlineKeyboardButton(text="Перейти на сайт", url=m_urls.iphone)
iphone_order_btn = telebot.types.InlineKeyboardButton(text="Заказать", callback_data="order iphone")

macbook_web_btn = telebot.types.InlineKeyboardButton(text="Перейти на сайт",url=m_urls.macbook)
macbook_order_btn = telebot.types.InlineKeyboardButton(text="Заказать", callback_data="order macbook")

apple_watch_web_btn = telebot.types.InlineKeyboardButton(text="Перейти на сайт", url=m_urls.apple_watch)
apple_watch_order_btn = telebot.types.InlineKeyboardButton(text="Заказать", callback_data="order apple_watch")

airpods_web_btn = telebot.types.InlineKeyboardButton(text="Перейти на сайт", url=m_urls.air_pods)
airpods_order_btn = telebot.types.InlineKeyboardButton(text="Заказать", callback_data="order air_pods")


buttons = [
    [ipad_web_btn, ipad_order_btn],
    [iphone_web_btn, iphone_order_btn],
    [macbook_web_btn, macbook_order_btn],
    [apple_watch_web_btn, apple_watch_order_btn],
    [airpods_web_btn, airpods_order_btn]
]