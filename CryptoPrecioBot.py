from telegram.ext import Updater, CommandHandler

# Esto es para que cuando el usuario meta el comando start, el bot le devuelve un mensaje.
def start(update, context): 

    update.message.reply_text('Hola, Bienvenido a CryptoPrice =D')


if __name__ == '__main__':

    updater = Updater(token='1735660439:AAE9i9bTaWkk-quX5VCrOC0SIqEHfhtZQT4', use_context=True)# Es para conectar el bot
    dp = updater.dispatcher # Se encarga de enviar las acciones EJ: cuando entras comandos.

    dp.add_handler(CommandHandler('start', start))# Esto es para que acive el comando xd.

    # Add Handler, Handler es una funcion que se ejecuta con alguna accion del usuario.
    updater.start_polling()
    updater.idle() # updater.star_polling() y updater.idle() es para que el bot quede escuchando.



