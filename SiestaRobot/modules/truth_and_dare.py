import html
import random
import SiestaRobot.modules.truth_and_dare_string as truth_and_dare_strin
import SiestaRobot.modules.game_strings as game_strings
from SiestaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SiestaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(game_strings.TRUTH_STRINGS))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(game_strings.DARE))

def sigma(update: Update, context: CallbackContext):
    update.effective_message.reply_video(random.choice(truth_and_dare_string.SIGMA))


def cosplay(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.COSPLAY))

def onepiece(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.WAIFU))



def tord(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(game_strings.TORD_STRINGS))

def wyr(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(game_strings.WYR_STRINGS))



TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
SIGMA_HANDLER = DisableAbleCommandHandler("sigma", sigma, run_async=True)
COSPLAY_HANDLER = DisableAbleCommandHandler("cosplay", cosplay, run_async=True)
WAIFU_HANDLER = DisableAbleCommandHandler("onepiece", onepiece, run_async=True)
WYR_HANDLER = DisableAbleCommandHandler("wyr", wyr, run_async=True)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord, run_async=True)





dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SIGMA_HANDLER)
dispatcher.add_handler(COSPLAY_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(WYR_HANDLER)
dispatcher.add_handler(TORD_HANDLER)
