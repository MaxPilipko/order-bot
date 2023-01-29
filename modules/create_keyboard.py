import telebot
import modules.create_buttons as m_button

start_bar = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                              row_width=1)
for button in m_button.buttons:
    start_bar.add(button)
    