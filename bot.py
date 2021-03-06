import config
import forest

bot = forest.bot
bot.report('Инициализация...')

from timeit import default_timer as timer

start_time = timer()

from modules.manybotslib import BotsRunner

bots = {
    'Лес': bot
}

runner = BotsRunner(admins=[config.creator], show_traceback=True)
runner.add_bots(bots)
runner.set_main_bot(bot, 'status')
bot.report('Готово! Боты запущены и готовы к работе.\nВремени использовано: {} секунд.'.format(timer() - start_time))
runner.run()
