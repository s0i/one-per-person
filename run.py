from core.search import Search

if __name__ == '__main__':
    bot = Search()
    
    while True:
        try:
            bot.run()
        except Exception as e:
            print(e)
            break