import datetime
import os

def main():
    if 'NEXT_DATE' in os.environ:
        if 'NEXT_TIME' in os.environ:
            #next_date_list = '2021','2','17'
            next_date_list = os.environ['NEXT_DATE'].split()

            next_date = datetime.datetime.strptime(next_date_list[0] + ' ' + next_date_list[1] + ' ' + next_date_list[2], '%Y %m %d').date()
            today = datetime.datetime.today().date()
            days_until_session = (next_date - today).days

            if days_until_session == 7:
                os.environ['MESSAGE'] = 'One week until the next session!'
            elif days_until_session == 0:
                os.environ['MESSAGE'] = 'Session today at ' + os.environ['NEXT_TIME']
            else: 
                os.environ['MESSAGE'] = str(days_until_session) + ' days until the next session, which will be on ' + next_date.strftime('%A %B %d, %Y') + ' at ' + os.environ['NEXT_TIME']

            os.system('python main.py')

        else:
            print('NEXT_TIME is a mandatory environment variable and is not set')
    else:
        print('NEXT_DATE is a mandatory environment variable and is not set')

main()